from smd.red import *

RED1 = 1
RED2 = 2

port = "COM10"
m = Master(port)

m.attach(Red(RED1))
m.attach(Red(RED2))

print("1 Numarali SMD")
print(m.scan_sensors(RED1))
print("2 Numarali SMD")
print(m.scan_sensors(RED2))