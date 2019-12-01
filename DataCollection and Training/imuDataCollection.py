from mpu6050 import mpu6050
sensor = mpu6050(0x68)

import time
#import training.py

imuData = open("imuDataAccel.txt","a")

active = True
counter = 0
label = ""

counter=input("Tell us the experiment number \n")
counter= int(counter)
while active:
    userInput=input("Enter E to exit otherwise T for true and F for false label. \n")
    if userInput == "E":
        active=False
    else: 
        print("recording data")
        if userInput == "T" :
            label = "True"
        elif userInput == "F":
            label = "False"
        imuData.write("\n")
        imuData.write(label)
        imuData.write(", ")
        # imuData.write(str(counter))
        # imuData.write(", ")
        startTime=time.time()
        while (time.time()-startTime) < 1.7 : 
            accel_data = sensor.get_all_data()[0]
            gyro_data = sensor.get_all_data()[1]

            imuData.write(str(accel_data['x']))
            imuData.write(", ")
            imuData.write(str(accel_data['y']))
            imuData.write(", ")
            imuData.write(str(accel_data['z']))
            imuData.write(", ")
            '''
            imuData.write(str(gyro_data['x']))
            imuData.write(", ")
            imuData.write(str(gyro_data['y']))
            imuData.write(", ")
            imuData.write(str(gyro_data['z']))
            imuData.write(", ")
            '''
            t
        
        counter +=1

