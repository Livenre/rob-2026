| Блок | Рядок коду |
|---|---|
| to draw_square | def draw_square(): |
| start drawing with pen on port Auto | pen_in5.down() |
| repeat 4 times | for count in range(4): |
| move steering with direction 0 and speed 10% | steering_drive.on(0, 10) |
| sleep for 0.2 seconds | time.sleep(0.2) |
| move steering with direction 0 and speed 25% | steering_drive.on(0, 25) |
| sleep for 0.3 seconds | time.sleep(0.3) |
| move steering with direction 0 and speed 40% | steering_drive.on(0, 40) |
| sleep for 2.5 seconds | time.sleep(2.5) |
| reset gyro on port 3 | gyro_sensor_in3.reset() |
| move steering with direction 100 and speed 20% | steering_drive.on(100, 20) |
| Wait until gyro angle on port 3 >= 90 | while not (gyro_sensor_in3.angle >= 90): pass |
| stop moving and hold | tank_drive.off(brake=True) |
| sleep for 0.5 seconds | time.sleep(0.5) |
| if gyro angle on port 3 > 90 | if gyro_sensor_in3.angle > 90: |
| move steering with direction -100 and speed 10% | steering_drive.on((-100), 10) |
| Wait until gyro angle on port 3 <= 90 | while not (gyro_sensor_in3.angle <= 90): pass |
| stop moving and hold | tank_drive.off(brake=True) |
| if gyro angle on port 3 < 90 | if gyro_sensor_in3.angle < 90: |
| move steering with direction 100 and speed 10% | steering_drive.on(100, 10) |
| Wait until gyro angle on port 3 >= 90 | while not (gyro_sensor_in3.angle >= 90): pass |
| stop moving and hold | tank_drive.off(brake=True) |
| sleep for 0.5 seconds | time.sleep(0.5) |






