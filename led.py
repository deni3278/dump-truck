import RPi.GPIO as GPIO

pin_red = 23
pin_yellow = 24
pin_green = 25

def initialize():
    GPIO.setup(pin_red, GPIO.OUT)
    GPIO.setup(pin_yellow, GPIO.OUT)
    GPIO.setup(pin_green, GPIO.OUT)

def red():
    GPIO.output(pin_red, GPIO.HIGH)
    GPIO.output(pin_yellow, GPIO.LOW)
    GPIO.output(pin_green, GPIO.LOW)

def yellow():
    GPIO.output(pin_red, GPIO.LOW)
    GPIO.output(pin_yellow, GPIO.HIGH)
    GPIO.output(pin_green, GPIO.LOW)

def green():
    GPIO.output(pin_red, GPIO.LOW)
    GPIO.output(pin_yellow, GPIO.LOW)
    GPIO.output(pin_green, GPIO.HIGH)

def off():
    GPIO.output(pin_red, GPIO.LOW)
    GPIO.output(pin_yellow, GPIO.LOW)
    GPIO.output(pin_green, GPIO.LOW)