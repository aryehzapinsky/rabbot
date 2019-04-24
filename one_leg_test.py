#!/usr/bin/env python3

import time

from PyLX_16a.lx16a import *

LX16A.initialize("/dev/cu.usbserial-1410")

servo1 = LX16A(1)
servo2 = LX16A(11)
servo3 = LX16A(13)

print("\
Servo 1 at: {}\n\
Servo 2 at: {}\n\
Servo 3 at: {}\n\
".format(servo1.getPhysicalPos(),
                            servo2.getPhysicalPos(),
                            servo3.getPhysicalPos()))

servo2.moveTimeWrite(90,time=2000)
time.sleep(2)
servo1.moveTimeWrite(20,time=2000)
time.sleep(2)
servo1.moveTimeWrite(180,time=2000)
time.sleep(2)

servo2.moveTimeWrite(180,time=2000)
time.sleep(2)
servo2.moveTimeWrite(20,time=2000)
time.sleep(2)

servo3.moveTimeWrite(180,time=2000)
time.sleep(2)
servo3.moveTimeWrite(20,time=2000)
time.sleep(2)
