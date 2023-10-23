from smd.red import*

port = "/dev/ttyUSB0"
m = Master(port)

m.attach(Red(1))
m.attach(Red(2))

m.set_shaft_cpr(1, 4741)
m.set_shaft_cpr(2, 4741)
m.set_shaft_rpm(1, 100)
m.set_shaft_rpm(2, 100)

m.set_operation_mode(1, OperationMode.PWM)
m.set_operation_mode(2, OperationMode.PWM)

print(m.scan_modules(1))
print(m.scan_modules(2))




CONTROL_MODE = 0
TUNE_MODE = 1

rgb_color = 0
rgb_cntr = 0
colors = [Colors.WHITE , Colors.BLUE]

mode = 0

torque = False
m.set_rgb(1, Index.RGB_1, colors[rgb_color])
while True:
    
    light = m.get_light(1, Index.Light_1)
    button = m.get_button(1, Index.Button_1)
    
    distance = m.get_distance(2, Index.Distance_1)
    joystick = m.get_joystick(2, Index.Joystick_1)
    IMU = m.get_imu(2, Index.IMU_1)
    
    
    
    #rgb change
    if light < 30:
        rgb_cntr += 1
    else:
        rgb_cntr = 0
    if rgb_cntr > 5:
        rgb_cntr = 0
        rgb_color +=1
        if rgb_color > 1:
            rgb_color = 0
        m.set_rgb(1, Index.RGB_1, colors[rgb_color])
        time.sleep(0.25)
        
    #mode change
    if button == 1:
        mode = rgb_color
    
    
    
    if mode == TUNE_MODE:
        m.pid_tuner(1)
        m.pid_tuner(2)
        
        time.sleep(27)
        mode = CONTROL_MODE
        
        rgb_color = 0
        m.set_rgb(1, Index.RGB_1, Colors.WHITE)
        
        
    if mode == CONTROL_MODE:
        if button == 1:
            if torque:
                torque = False
            else:
                torque = True
            m.enable_torque(1, torque)
            m.enable_torque(2, torque)
            time.sleep(0.25)
            
        m.enable_torque(1, torque)
        m.enable_torque(2, torque)
        
        
        pwm1 = joystick[0]*100 - 50
        pwm2 = joystick[1]*100 - 50
        if(joystick[0] < 0.60 and joystick[0] > 0.39):
            pwm1 = 0
        if(joystick[1] < 0.60 and joystick[1] > 0.39):
            pwm2 = 0
            
        pwm1 += IMU[0]
        pwm2 += IMU[1]
        
        if distance < 20:
            m.enable_torque(1, False)
            m.enable_torque(2, False)
            pwm1 = 0
            pwm2 = 0
        
        m.set_duty_cycle(1, pwm1)
        m.set_duty_cycle(2, pwm2)
        
        
    print(str(light) + "\t" + str(button) + "\t" + str(joystick))