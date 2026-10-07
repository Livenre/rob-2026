from ev3dev2.motor import MoveTank, OUTPUT_A, OUTPUT_B, SpeedPercent
from ev3dev2.sensor import INPUT_2, INPUT_3
from ev3dev2.sensor.lego import UltrasonicSensor, GyroSensor
import time

tank = MoveTank(OUTPUT_A, OUTPUT_B)
ultra = UltrasonicSensor(INPUT_2)
gyro = GyroSensor(INPUT_3)
time.sleep(0.5)

stan = "poshuk"
vkhid = time.time()

def perekhid(novyi):
    global stan, vkhid
    print(f"{stan} -> {novyi}")
    stan = novyi
    vkhid = time.time()
    
    if novyi == "vidmova":
        tank.off()
    elif novyi == "rozvorot":
        gyro.reset()


print(f"Початок: {stan}")

while stan != "gotovo":
    d = ultra.distance_centimeters

    if stan == "poshuk":              
        tank.on(SpeedPercent(30), SpeedPercent(30))
        if d <= 20:
            perekhid("pidhid")

    elif stan == "pidhid":            
        tank.on(SpeedPercent(10), SpeedPercent(10))
        if d <= 15:
            tank.off()
            perekhid("rozvorot")
        elif time.time() - vkhid > 3.5:
            print(f"Стіна дуже близько!!! ")
            perekhid("vidmova")
            
    elif stan == "vidmova":
        tank.on(SpeedPercent(-20), SpeedPercent(-20))
        if time.time() - vkhid > 1.5: 
            tank.off()
            perekhid("rozvorot")

    elif stan == "rozvorot":          
        tank.on(SpeedPercent(20), SpeedPercent(-20))
        if gyro.angle >= 88: # Із-за інерції робимо з запасом
            tank.off()
            perekhid("gotovo")

    if time.time() - vkhid > 20:      
        print("таймаут у стані", stan)
        tank.off()
        break
