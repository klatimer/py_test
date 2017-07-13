import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)
GPIO.setup(17, GPIO.IN, pull_up_down = GPIO.PUD_UP)

while GPIO.input(17):
	GPIO.output(18, GPIO.HIGH)
	time.sleep(0.5)
	GPIO.output(18, GPIO.LOW)
	time.sleep(0.5)

print("button pressed... stopping blink")
GPIO.cleanup()
