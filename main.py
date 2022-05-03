import time
import gauge
import led
import servo
import RPi.GPIO as GPIO

low = 50
high = 150
pour = 10
pin_button = 21

print("") # new line

def initialize():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(pin_button, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

    gauge.initialize()
    led.initialize()
    servo.initialize()
    gauge.calibrate()

try:
    initialize()

    while True:
        print("Press the button to start measuring.")

        GPIO.wait_for_edge(pin_button, GPIO.FALLING)

        grams = gauge.measure()

        print("Measured " + str(grams) + " g.")

        if grams <= low:
            led.green()
        elif low < grams < high:
            led.yellow()
        elif grams <= high:
            led.red()

        while grams > pour:
            grams -= pour

            servo.turn()
            time.sleep(1)
            servo.reset()

            print("Poured " + str(pour) + " g. Weight is now at " + str(grams) + " g.")

            time.sleep(1)

        led.off()
finally:
    servo.cleanup()
    GPIO.cleanup()