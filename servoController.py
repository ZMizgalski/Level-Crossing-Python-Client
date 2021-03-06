# pip3 install adafruit-circuitpython-motor
# pip3 install adafruit-circuitpython-pca9685
# pip3 install Adafruit-Blinka
# pip3 install adafruit-blinka

import time

from board import SCL, SDA
import busio

from adafruit_motor import servo
from adafruit_pca9685 import PCA9685


class MotorControl(object):
    def __init__(self, angle=0, frequency=50):
        self.angle = angle
        self.frequency = frequency
        self.i2c = busio.I2C(SCL, SDA)
        self.pca = PCA9685(self.i2c)
        self.pca.frequency = self.frequency
        self.servo5 = servo.Servo(self.pca.channels[5])
        self.servo1 = servo.Servo(self.pca.channels[1])
        self.servo8 = servo.Servo(self.pca.channels[8])
        self.servo11 = servo.Servo(self.pca.channels[11])

    def open(self):
        self.servo5.angle = 90 + self.angle
        self.servo1.angle = 90 - self.angle
        self.servo8.angle = 90 + self.angle
        self.servo11.angle = 90 - self.angle
        time.sleep(0.03)

    def close(self):
        self.servo5.angle = 90
        self.servo1.angle = 90
        self.servo8.angle = 90
        self.servo11.angle = 90
        time.sleep(0.03)
