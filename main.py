#! /usr/bin/python3

import temperature
import schedule
import datetime
from gpiozero import LED

s = temperature.init()
furnace = LED(4)
hysteresis = 0.5

while 1:
	print(datetime.datetime.now())
	actual = temperature.read(s)
	print("current temp is", actual)
	desired = schedule.get()
	if (actual - desired) > hysteresis:
		# Turn off furnace
		# Note: This may result in over-heating, since the
		# furnace does not turn off immidiately, but keeps
		# the blower on for a few minutes to cool down
		furnace.off()
		print("Turning furnace off...")

	elif (desired - actual) > hysteresis:
		# Turn on furnace
		furnace.on()
		print("Turning furnace on...")
	
