# Kenneth Latimer
# 1/16/17

import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)

GPIO.setup(18, GPIO.OUT)
GPIO.setup(17, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)


