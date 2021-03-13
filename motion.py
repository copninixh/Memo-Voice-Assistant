import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
#Set GPIO PIN Connect on Raspi
PIR_PIN = 4
#Set Your Pin = Input
GPIO.setup(PIR_PIN, GPIO.IN)


try:
    print("c")
    time.sleep(2)
    print("Ready")
    while True:
        if GPIO.input(PIR_PIN):
            print("Detect Object 6m in 120 ")
            time.sleep(1)

except KeyboardInterrupt:
    print ("q")
    GPIO.cleanup()

