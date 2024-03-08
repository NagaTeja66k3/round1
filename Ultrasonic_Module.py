import RPi.GPIO as GPIO
import time
class UltrasonicModule(object):
    '''Ultrasonic distance measurement module'''
    def __init__(self, trig_pin, echo_pin):
        self.trig_pin = trig_pin
        self.echo_pin = echo_pin
        self.pins_for_motor = [5, 6, 13, 19, 21, 22, 23, 24]  # These pins are occupied by the motor module
        self.pins_available = [12, 16, 17, 18, 20, 25, 26, 27]
    def setup(self):
        '''Pin initialization'''
        if (self.trig_pin not in self.pins_for_motor) and (self.trig_pin in self.pins_available):
            print("trig_pin is valid")
        else:
            print("trig_pin is invalid")
            return False
        if (self.echo_pin not in self.pins_for_motor) and (self.echo_pin in self.pins_available):
            print("echo_pin is valid")
        else:
            print("echo_pin is invalid")
            return False
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        GPIO.setup(self.trig_pin, GPIO.OUT, initial=GPIO.LOW)  # Initialize trigger pin to low level
        GPIO.setup(self.echo_pin, GPIO.IN)
        return True
    def get_distance(self):
        '''Polling method to obtain distance'''
        GPIO.output(self.trig_pin, GPIO.HIGH)
        time.sleep(0.000015)
        GPIO.output(self.trig_pin, GPIO.LOW)
        while not GPIO.input(self.echo_pin):
            pass
        t1 = time.time()  # Start timing
        while GPIO.input(self.echo_pin):
            pass
        t2 = time.time()
        distance = (t2 - t1) * 340 / 2  # Calculate distance based on the speed of sound propagation
        return distance