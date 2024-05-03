# SPDX-FileCopyrightText: Copyright (c) 2020 Bryan Siepert for Adafruit Industries
#
# SPDX-License-Identifier: MIT
import time
import board
from adafruit_lsm6ds.lsm6dsox import LSM6DSOX
import serial 

i2c = board.I2C()  # uses board.SCL and board.SDA
# i2c = board.STEMMA_I2C()  # For using the built-in STEMMA QT connector on a microcontroller
sensor = LSM6DSOX(i2c)
threshold = 9.7 # threshold were using for acceleration 
consecutive_threshold = 1 # number of times it needs to exceed at least
count_exceed = 0 
#state = 0 

arduino = serial.Serial(port='COM4', baudrate = 115200, timeout = 1)

while True:
    #check sensor data
    acceleration = sensor.acceleration
    # if state == 0:
    #     if any(abs(a) > threshold for a in acceleration):
    #         state == 1
    
    # else:
    #     if any(abs(a) < threshold for a in acceleration):
    #         state == 0
    #gyro = sensor.gyro
    exceed_threshold = 0 


    #check if acceleration is greater than threshold
    if any(abs(a) > threshold for a in acceleration):
        count_exceed += 1
    else:
        count_exceed = 0

    while count_exceed >= consecutive_threshold:
        exceed_threshold = 1 
        count_exceed = 0 # reset counter 

    ser.write(str(exceed_threshold).encode()) #serially send the string of the state

    print("Acceleration: X:%.2f, Y: %.2f, Z: %.2f m/s^2" % (sensor.acceleration))
    print("Gyro X:%.2f, Y: %.2f, Z: %.2f radians/s" % (sensor.gyro))
    print("Exceed threshold: %d" %exceed_threshold) #print if acceleration exceeds threshold. 
    print("")
    time.sleep(0.5)

#terminal check sensor outputting to bus 1 
