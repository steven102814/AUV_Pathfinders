# SPDX-FileCopyrightText: Copyright (c) 2020 Bryan Siepert for Adafruit Industries
#
# SPDX-License-Identifier: MIT
import time
import board
from adafruit_lsm6ds.lsm6dsox import LSM6DSOX

i2c = board.I2C()  # uses board.SCL and board.SDA
# i2c = board.STEMMA_I2C()  # For using the built-in STEMMA QT connector on a microcontroller
sensor = LSM6DSOX(i2c)
threshold = 3 # threshold were using for acceleration 

while True:
    #check sensor data
    acceleration = sensor.acceleration
    gyro = sensor.gyro

    #check if acceleration is greater than threshold
    if any(abs(x) > threshold for x in acceleration):
        exceed_threshold = 1
    else:
        exceed_threshold = 0

    print("Acceleration: X:%.2f, Y: %.2f, Z: %.2f m/s^2" % (sensor.acceleration))
    print("Gyro X:%.2f, Y: %.2f, Z: %.2f radians/s" % (sensor.gyro))
    print("Exceed Threshold: %d" % exceed_threshold) #print if acceleration exceeds threshold. 
    print("")
    time.sleep(0.5)

#terminal check sensor outputting to bus 1 
