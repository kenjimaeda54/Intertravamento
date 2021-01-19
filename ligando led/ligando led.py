import RPi.GPIO as GPIO
from time import *

LED = 24
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED, GPIO.OUT)

while True:
 GPIO.output(LED,1)