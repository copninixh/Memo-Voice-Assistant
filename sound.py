import RPi.GPIO as GPIO
import time

enablePin = 16

try:
    while True:
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(enablePin , GPIO.OUT)
        GPIO.output(enablePin, 1)
        time.sleep(1)
        GPIO.output(enablePin, 0)
        for cnt in range(1, 30):
            time.sleep(0.5)
        
except KeyboardInterrupt:
    print("Program terminated")
    GPIO.cleanup()

    
