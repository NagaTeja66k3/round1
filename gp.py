import RPi.GPIO as GPIO  # Import the GPIO module
GPIO.setmode(GPIO.BCM)  # Set the numbering mode to BCM
GPIO.setwarnings(False)  # Turn off warnings
GPIO.setup(1, GPIO.IN)  # Set pin 1 (BCM numbering) as an input channel
GPIO.setup(2, GPIO.OUT)  # Set pin 2 as an output channel
value = GPIO.input(1)  # Read the input value of channel 1 (0 / GPIO.LOW / False or 1 / GPIO.HIGH / True)
GPIO.output(2, GPIO.HIGH)  # Set the output of channel 2 to a high logic level (0 / GPIO.LOW / False or 1 / GPIO.HIGH / True)
GPIO.cleanup()  # Clean up channel resources