from smd.red import*

port = "/dev/ttyUSB0"

m = Master(port)

m.attach(Red(0))

m.set_operation_mode(0,OperationMode.PWM)

m.eeprom_write(0)