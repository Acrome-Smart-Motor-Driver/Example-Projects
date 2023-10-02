from move_math import *
import threading
from smd.red import *

port = "COM12"
m = Master(port)

#We need to know the IDs of the SMDs used
m.scan()
linear_ID = 0                 
dc1_ID = 1
dc2_ID = 2

# setting the operation modes of SMDs
m.set_operation_mode(linear_ID, OperationMode.PWM)       
m.set_operation_mode(dc1_ID, OperationMode.Velocity)
m.set_operation_mode(dc2_ID, OperationMode.Velocity)

def driveID():
    while True:
        for t in timePoints :
            m.set_duty_cycle(id, Sin_pwm80(t))
            time.sleep(0.1)


def driveID1():
    while True:
        for t in timePoints :
            m.set_velocity(id, SinVelocity(t))
            time.sleep(0.1)
    

def driveID2():
    while True:
        for t in timePoints :
            m.set_velocity(id, SinVelocity(t))
            time.sleep(0.1)

m.enable_torque(linear_ID, True)    #enables the motor torque to start rotating
m.enable_torque(dc1_ID, True)
m.enable_torque(dc2_ID, True)       
 
if __name__ =="__main__":
    t1 = threading.Thread(target=driveID, args=())
    t2 = threading.Thread(target=driveID1, args=())
    t3 = threading.Thread(target=driveID2, args=())
 
    t1.start()
    t2.start()
    t3.start()
 
    t1.join()
    t2.join()
    t3.join()
 
    print("Done!")
