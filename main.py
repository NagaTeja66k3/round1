#!/usr/bin/python3
"""
Simple script to control a car with ultrasonic obstacle avoidance using Raspberry Pi GPIO.
"""
import RPi.GPIO as GPIO
import sys
import time
import Ultrasonic_Module as Ul
import Motor_Module as Mo

### Module Initialization
ultrasonic_front = Ul.Ultrasonic_Module(25, 26)  # Create an ultrasonic module object for the front sensor
ultrasonic_right = Ul.Ultrasonic_Module(17, 27)  # Create an ultrasonic module object for the right sensor
ultrasonic_left = Ul.Ultrasonic_Module(22, 23)  # Create an ultrasonic module object for the left sensor

motor = Mo.Motor_Module()  # Create a motor module object

print("######### Initiating the ultrasonic modules... ##########")
# Initialize the ultrasonic modules
if not ultrasonic_front.setup() or not ultrasonic_right.setup() or not ultrasonic_left.setup():
    print("Ultrasonic setup failed, program stopped.")
    exit()

print("######### Initiating the motor module... ##########")
motor.setup()  # Initialize the motor module

### Initially, the car is in the forward state
print("The car starts running...")
motor.ahead()

### Loop to check distance
distance_front = 10
distance_right = 10
distance_left = 10
limited_distance = 0.05  # Minimum obstacle distance
time_rear = 0.8  # Duration for moving backward
time_right = 1.2  # Duration for turning right
time_left = 1.2  # Duration for turning left

try:
    while True:
        distance_front = ultrasonic_front.getdistance()  # Get the current distance from the front sensor
        distance_right = ultrasonic_right.getdistance()  # Get the current distance from the right sensor
        distance_left = ultrasonic_left.getdistance()  # Get the current distance from the left sensor

        if distance_front <= limited_distance:
            print("Run into an obstacle in front")
            motor.stop()  # Stop the motor
            motor.rear(time_rear)  # Move backward for a period
            motor.right(time_right)  # Turn right for a period
            motor.ahead()  # Resume forward state

        elif distance_right <= limited_distance:
            print("Obstacle detected on the right")
            motor.stop()  # Stop the motor
            motor.left(time_left)  # Turn left for a period
            motor.ahead()  # Resume forward state

        elif distance_left <= limited_distance:
            print("Obstacle detected on the left")
            motor.stop()  # Stop the motor
            motor.right(time_right)  # Turn right for a period
            motor.ahead()  # Resume forward state

except KeyboardInterrupt:
    motor.stop()  # Stop the motor on keyboard interrupt
    print("\nStop the car")

    # Clean up GPIO resources
    GPIO.cleanup()
