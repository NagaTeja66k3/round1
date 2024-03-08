import RPi.GPIO as GPIO
import time
import sys
class MotorModule(object):
    '''Motor control module'''
    def __init__(self):
        # Pins for enable and control
        self.enable_pins = [5, 6, 13, 19]
        self.control_pins = [21, 22, 23, 24]
        # Pins for four directions
        self.right_ahead_pin = self.control_pins[3]
        self.right_back_pin = self.control_pins[2]
        self.left_ahead_pin = self.control_pins[1]
        self.left_back_pin = self.control_pins[0]
        # Initialize pins
        self.setup()
    def setup(self):
        '''Pin initialization'''
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        # Initialize control pins to low level
        for pin in self.control_pins:
            GPIO.setup(pin, GPIO.OUT)
            GPIO.output(pin, GPIO.LOW)
        # Initialize enable pins to high level
        for pin in self.enable_pins:
            GPIO.setup(pin, GPIO.OUT)
            GPIO.output(pin, GPIO.HIGH)
    def ahead(self, second_value=0):
        '''Car moves forward'''
        self.setup()
        GPIO.output(self.right_ahead_pin, GPIO.HIGH)
        GPIO.output(self.left_ahead_pin, GPIO.HIGH)
        if second_value != 0:
            time.sleep(second_value)
            self.stop()
    def left(self, second_value=0):
        '''Car moves left'''
        self.setup()
        GPIO.output(self.right_ahead_pin, GPIO.HIGH)
        if second_value != 0:
            time.sleep(second_value)
            self.stop()
    def right(self, second_value=0):
        '''Car moves right'''
        self.setup()
        GPIO.output(self.left_ahead_pin, GPIO.HIGH)
        if second_value != 0:
            time.sleep(second_value)
            self.stop()
    def rear(self, second_value=0):
        '''Car moves backward'''
        self.setup()
        GPIO.output(self.right_back_pin, GPIO.HIGH)
        GPIO.output(self.left_back_pin, GPIO.HIGH)
        if second_value != 0:
            time.sleep(second_value)
            self.stop()
    def stop(self):
        '''Stop the car'''
        for pin in self.control_pins:
            GPIO.output(pin, GPIO.LOW)