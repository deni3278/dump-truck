import RPi.GPIO as GPIO

servo_pin = 19
pwm: GPIO.PWM

def initialize():
    GPIO.setup(servo_pin, GPIO.OUT)

    global pwm
    pwm = GPIO.PWM(servo_pin, 50)
    pwm.start(0.8)  # 0 degrees

def reset():
    pwm.ChangeDutyCycle(0.8) # 0 degrees

def turn():
    pwm.ChangeDutyCycle(10.8) # 180 degrees

def cleanup():
    pwm.ChangeDutyCycle(0)
    pwm.stop()