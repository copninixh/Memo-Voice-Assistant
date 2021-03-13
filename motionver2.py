from gpiozero import MotionSensor

pir = MotionSensor(4)

try:
    while True:
        pir.wait_for_motion()
        print("Detect Object in 6m 120 radius")
        pir.wait_for_no_motion()
        print("No Detect")
except KeyboardInterrupt:

    print("q")


