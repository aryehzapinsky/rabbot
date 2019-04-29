import json
import datetime

from PyLX_16a.lx16a import *

class Recorder():
    LX16A.initialize("/dev/ttyUSB0")
    motor_numbers = [11, 12, 13,
                     21, 22, 23,
                     31, 32, 33]
    motors = [LX16A(motor_num) for motor_num in motor_numbers]

    clean_sequence = {"name": "",
                      11: [],
                      12: [],
                      13: [],
                      21: [],
                      22: [],
                      23: [],
                      31: [],
                      32: [],
                      33: []}

    sequence = {"name": "",
                11: [],
                12: [],
                13: [],
                21: [],
                22: [],
                23: [],
                31: [],
                32: [],
                33: []}

    # @classmethod
    # def initialize(cls):
    #     LX16A.initialize("/dev/cu.usbserial-1410")
    #     cls.motor_numbers = [11, 12, 13,
    #                  21, 22, 23,
    #                  31, 32, 33]
    #     for motor_num in cls.motor_numbers:
    #         cls.motors.append(LX16A(motor_num))
    #         print("{}\n".format(cls.motors[-1]))

    @classmethod
    def save_sequence(cls, name):
        time_str = datetime.datetime.strftime(datetime.datetime.now(), "%m_%d_%H_%M")
        cls.sequence['name'] = "{}--{}".format(time_str, name)

        with open('sequences.txt', "a+") as fp:
            json.dump(cls.sequence, fp)
            fp.write('\n')
            fp.flush()

        cls.sequence = cls.clean_sequence

    @classmethod
    def reset_sequence(cls):
        cls.sequence = cls.clean_sequence

    @classmethod
    def start_motors(cls):
        for motor in cls.motors:
            motor.loadOrUnloadWrite(1)

    @classmethod
    def stop_motors(cls):
        for motor in cls.motors:
            motor.loadOrUnloadWrite(0)

    @classmethod
    def record_positions(cls):
        for motor, motor_num in zip(cls.motors, cls.motor_numbers):
            cls.sequence[motor_num].append(motor.getPhysicalPos())
