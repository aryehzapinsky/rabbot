import json
import time

from PyLX_16a.lx16a import *

class Player():
    LX16A.initialize("/dev/cu.usbserial-1410")
    motor_numbers = [11, 12, 13,
                     21, 22, 23,
                     31, 32, 33]
    motors = [LX16A(motor_num) for motor_num in motor_numbers]

    sequences_dict = {}

    @classmethod
    def read_sequences(cls):
        with open('sequences.txt', "r") as fp:
            for line in fp:
                sequence = json.loads(line)
                name = sequence.pop("name")
                cls.sequences_dict.update({name: sequence})

    @classmethod
    def get_sequences(cls):
        cls.read_sequences()
        return cls.sequences_dict

    @classmethod
    def play_sequence(cls, name, backwards=False):
        sequence = cls.sequences_dict.get(name)
        steps = range(len(sequence.get('11')))
        steps = list(steps) if not backwards else list(reversed(steps))
        for step in steps:
            for motor, motor_num in zip(cls.motors, cls.motor_numbers):
                dur = 2000
                motor.moveTimeWrite(sequence[str(motor_num)][step], dur)
            time.sleep(2)
