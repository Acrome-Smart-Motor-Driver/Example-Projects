from smd.red import*
from osModules import*

INPUTid = False

port = USB_serial_port()
print(port)


m = Master(port, 115200)

print(m.scan())

while not INPUTid:
    try:
        new_id = int(input('update id of connected smd to : '))
        INPUTid = True
    except:
        print('it is not excepted id!')



m.scan()
m.update_driver_id(m.attached()[0], new_id)

m.attach(Red(new_id))

try:
    info = m.get_driver_info(new_id)
    print(info)
    if info != None:
        print("it's done.")
    else:
        print("it's not None")
except:
    print(info)
    print("error.")



