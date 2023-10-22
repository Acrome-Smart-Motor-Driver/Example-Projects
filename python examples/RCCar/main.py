from smd.red import*
import time
port = "/dev/ttyUSB0"
m = Master(port)
m.attach(Red(0))

m.scan_modules(0)

distanceID = Index.Distance_1
servoID = Index.Servo_1



def car_back():
    m.set_servo(0,180)
    time.sleep(0.5)
    m.set_duty_cycle(0,-40)
    time.sleep(3)
    m.set_servo(0.90)
    time.sleep(0.5)


def car_forward():
    m.set_duty_cycle(0,60)


m.set_servo(0, 90)
m.enable_torque(0,True)

while True:
    distance = m.get_distance(0)

    if distance <= 20:
        car_back()

    else:
        car_forward()

    time.sleep(0.2)


