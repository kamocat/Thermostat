#! /usr/bin/python3

import display
import temperature
import schedule
import datetime
import time
from gpiozero import LED

s = temperature.init()
furnace = LED(4)
hysteresis = 0.5
desired = 0
actual = 100

while 1:
	if (actual - desired) > hysteresis:
		# Turn off furnace
		# Note: This may result in over-heating, since the
		# furnace does not turn off immidiately, but keeps
		# the blower on for a few minutes to cool down
		furnace.off()
		#print("Turning furnace off...")
	elif (desired - actual) > hysteresis:
		# Turn on furnace
		furnace.on()
		#print("Turning furnace on...")
	# Send update to the display
	display.update(str(round(desired,1)), str(round(actual,1)))
	display.outside()
	# Sleep for several seconds
	time.sleep(3)
	actual = temperature.read(s)
	#print(datetime.datetime.now().time(), "current temp is", actual)
	try:
		desired = schedule.get()
	except:
		print("Google Calendar timed out.")
	
