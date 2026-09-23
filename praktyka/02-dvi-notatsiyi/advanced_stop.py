from ev3dev2.motor import MoveTank, OUTPUT_A, OUTPUT_B, SpeedPercent
from ev3dev2.sensor import INPUT_1, INPUT_2, INPUT_3
from ev3dev2.sensor.lego import UltrasonicSensor, ColorSensor, GyroSensor
import time

tank = MoveTank(OUTPUT_A, OUTPUT_B)
ultra = UltrasonicSensor(INPUT_2)
color = ColorSensor(INPUT_1)
gyro = GyroSensor(INPUT_3)

time.sleep(0.5)

# З кодом допомогав ШІ

# Трек П: Оформлення руху до перешкоди як функції
def drive_to_obstacle(stopping_threshold, max_speed=30):
    print(f"\n-_-_- СТАРТ. Ціль: зупинка на {stopping_threshold} см -_-_-")
    
    # Трек П: З якої відстані починається гальмування
    stopping_distance = stopping_threshold + 40
    last_print_time = time.time()

    # d: Використовуємо while, а не on_for_seconds, щоб постійно опитувати датчики
    while True:
        distance = ultra.distance_centimeters
        color_brightness = color.reflected_light_intensity
        
        # b: Друк відстані щосекунди
        current_time = time.time()
        if current_time - last_print_time >= 1.0:
            print(f"Їду... Відстань: {distance:.1f} см")
            last_print_time = current_time

        # h: Комбінація датчиків (якщо бачимо лінію раніше за перешкоду)
        if color_brightness < 20: 
            tank.off()
            print(f"Стоп. Знайдено лінію (яскравість {color_brightness})")
            break
            
        # Ультразвук: перевірка порогу зупинки
        if distance <= stopping_threshold:
            distance_trigger = distance
            tank.off()
            
            # e: Вимірювання затримки реакції
            time.sleep(0.5) 
            fact_distance = ultra.distance_centimeters
            print(f"Тригер на {distance_trigger:.1f} см. Фактична зупинка: {fact_distance:.1f} см")
            print(f"Затримка реакції (інерція): {distance_trigger - fact_distance:.1f} см")
            break
            
        # Трек П: Плавна зупинка (пропорційне гальмування)
        elif distance <= stopping_distance:
            speed = (distance - stopping_threshold) * 1.5 
            if speed < 5: speed = 5
            if speed > max_speed: speed = max_speed
            tank.on(SpeedPercent(speed), SpeedPercent(speed))
            
        # Далеко від перешкоди - їдемо на заданій швидкості
        else:
            tank.on(SpeedPercent(max_speed), SpeedPercent(max_speed))
            
        time.sleep(0.05)

    # --------------------------------------
    
    # a: Здати назад на 5 см
    print("-_-_- Здаю назад на 5 см -_-_-")
    tank.on_for_seconds(SpeedPercent(-20), SpeedPercent(-20), 1.0)
    time.sleep(0.5)
    
    # g: Розвернути робота на 180° і проїхати тим самим шляхом назад
    print("-_-_- Розворот на 180° по гіроскопу -_-_-")
    gyro.reset()
    tank.on(SpeedPercent(20), SpeedPercent(-20))
    while gyro.angle < 179:
        pass
    tank.off()
    time.sleep(0.5)
    
    print("-_-_- Їду тим самим шляхом назад -_-_-")
    tank.on_for_seconds(SpeedPercent(max_speed), SpeedPercent(max_speed), 3.0)

# Трек П, перевірка порога на 10 і на 25 см 
drive_to_obstacle(stopping_threshold=10)
# drive_to_obstacle(stopping_threshold=25)

# c: Зміна порогу на 5 і на 30 см 
# drive_to_obstacle(stopping_threshold=5, max_speed=30)
# drive_to_obstacle(stopping_threshold=30, max_speed=30)

# f: Збільшення швидкісті з 30 до 60
# drive_to_obstacle(stopping_threshold=15, max_speed=60)
