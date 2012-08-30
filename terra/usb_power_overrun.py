import ablib
import time

power_overrun = ablib.Pin('W','9','in')

while True:
	if power_overrun.get_value()==False:
		print "Power overrun !";
		time.sleep(1)

