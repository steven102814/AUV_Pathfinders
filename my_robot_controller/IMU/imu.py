# SPDX-FileCopyrightText: Copyright (c) 2020 Bryan Siepert for Adafruit Industries
#
# SPDX-License-Identifier: MIT
import time
import board
from adafruit_lsm6ds.lsm6dsox import LSM6DSOX
#Simport serial
import serial.tools.list_ports

i2c = board.I2C()  # uses board.SCL and board.SDA
# i2c = board.STEMMA_I2C()  # For using the built-in STEMMA QT connector on a microcontroller
sensor = LSM6DSOX(i2c)
threshold = 9.7 # threshold were using for acceleration 
consecutive_threshold = 1 # number of times it needs to exceed at least
count_exceed = 2 
#state = 0 

arduino = serial.Serial(port='/dev/ttyACM0', baudrate = 9600, timeout = 1)
#arduino = serial.Serial()
#arduino.baudrate = 9600
#arduino.port = '/dev/ttyACM0'
#arduino.open()

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
    exceed_threshold = 2


    #check if acceleration is greater than threshold
    if any(abs(a) > threshold for a in acceleration):
        count_exceed += 1
    else:
        count_exceed = 0

    while count_exceed >= consecutive_threshold:
        exceed_threshold = 1 
        count_exceed = 0 # reset counter 
    #exceed_threshold = int (exceed_threshold)
    #command = int(input("Arduino"))
    arduino.write([exceed_threshold]) #serially send the string of the state
    #arduino.write([exceed_threshold]) #serially send the string of the state

    ### data 
    data = arduino.read()
    
    if data:
        print((data))
    

    print("Acceleration: X:%.2f, Y: %.2f, Z: %.2f m/s^2" % (sensor.acceleration))
    print("Gyro X:%.2f, Y: %.2f, Z: %.2f radians/s" % (sensor.gyro))
    print("Exceed threshold: %d" %exceed_threshold) #print if acceleration exceeds threshold. 
    #print("Exceed threshold:" int(exceed_threshold))
    print("")
    time.sleep(0.5)

#terminal check sensor outputting to bus 1 
