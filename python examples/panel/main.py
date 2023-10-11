from smd.red import *
import time


colorss = [Colors.RED, Colors.BLUE, Colors.CYAN, Colors.MAGENTA, Colors.WHITE]

RED1 = 1
RED2 = 2

port = "COM10"
m = Master(port)

m.attach(Red(RED1))
m.attach(Red(RED2))

m.set_operation_mode(RED1, OperationMode.PWM)
m.set_operation_mode(RED2, OperationMode.Position)

m.set_shaft_cpr(RED1, 4741)
m.set_shaft_cpr(RED2, 4741)
m.set_shaft_rpm(RED1, 100)
m.set_shaft_rpm(RED2, 100)

"""
m.pid_tuner(RED1)
m.pid_tuner(RED2)
time.sleep(30)
"""
rgb_cnt = 0
rgb_index = 0
velocity_sp = 0

while True:
    """reading modules"""
    distance = m.get_distance(RED2 , Index.Distance_1)
    button = m.get_button(RED2, Index.Button_3)
    light = m.get_light(RED1, Index.Light_1)
    joystick = m.get_joystick(RED2, Index.Joystick_1)
    
    
    if (light < 50):
        rgb_cnt +=1
    if rgb_cnt > 5:
        rgb_index +=1
        rgb_cnt = 0
    if rgb_index > 4:
        rgb_index = 0

    #Table
    #print(distance)
    #print(joystick[1])

    m.set_rgb(RED1, Index.RGB_1  ,colorss[rgb_index])

    """
    print(button)
    print(light)
    """
    if button == 1:
        torque = True
    else:
        torque = False
    
    m.enable_torque(RED1, torque)
    m.enable_torque(RED2, torque)


    velocity_sp = joystick[1]*100 -50
    print(velocity_sp)

    # Control
    m.set_position(RED2, distance*20)
    m.set_duty_cycle(RED1, int(velocity_sp))

    #time.sleep(0.5)

    #m.set_position(RED1, )