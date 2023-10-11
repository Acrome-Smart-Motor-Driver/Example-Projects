from smd.red import*

port = "COM10"

m = Master(port)

m.attach(Red(0))

m.update_driver_id(0, 1)

