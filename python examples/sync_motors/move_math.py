import math
import decimal
import time
from smd.red import *

def float_range(start, stop, step):
  while start < stop:
    yield float(start)
    start += decimal.Decimal(step)

timePoints = list(float_range(0, 4.18, '0.1'))

def SinVelocity(x):
    final = 50*math.sin((1.5)*x)
    if final < 0:
        return -1 * final
    else:
        return final
    
def Sin_pwm80(x):
    final = 80*math.sin((1.5)*x)
    return final




