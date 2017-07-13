# Kenneth Latimer
# 1/16/17
# Description:
# 	Using two threads to flash an LED and stop once button is pressed

import RPi.GPIO as GPIO
import time
import threading

global exitFlag
exitFlag = False

class blinkThread (threading.Thread):
	def __init__(self, name):
		threading.Thread.__init__(self)
		self._running = True
		self.name = name
	def terminate(self):
		self._running = False
	def run(self):
		global exitFlag
		print "Starting " + self.name
		while not exitFlag:
			try:
				GPIO.output(18, GPIO.HIGH)
				time.sleep(0.5)	
				GPIO.output(18, GPIO.LOW)
				time.sleep(0.5)
			except RuntimeError:
				pass
		print "Exiting " + self.name

class interruptThread (threading.Thread):
	def __init__(self, name):
		threading.Thread.__init__(self)
		self._running = True
		self.name = name
	def terminate(self):
		self._running = False
	def run(self):
		global exitFlag
		print "Starting " + self.name
		GPIO.wait_for_edge(17, GPIO.FALLING)
		exitFlag = True
		print "Exiting " + self.name

if __name__ == "__main__":
	GPIO.setmode(GPIO.BCM)
	GPIO.setup(18, GPIO.OUT) #LED output
	GPIO.setup(17, GPIO.IN, pull_up_down = GPIO.PUD_UP) #Button input
	# Create threads
	bt = blinkThread("LED blink thread")
	it = interruptThread("interrupt thread")
	# Start threads
	bt.start()
	it.start()
	# Check for exit flag
	while not exitFlag: # May need to make this more robust
		time.sleep(0.1)
		if exitFlag:
			bt.terminate()
			it.terminate()
	# Main thread finished
	print "Exiting Main Thread"
	GPIO.cleanup()
