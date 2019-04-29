from PyLX_16a.lx16a import *  

LX16A.initialize("/dev/ttyUSB0") 
motor_numbers = [11,12,13,21,22,23,31,32,33]  
motors= [LX16A(motor_num) for motor_num in motor_numbers]  
