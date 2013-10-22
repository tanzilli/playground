from time import sleep
from ablib import Pin

power_overrun = Pin('W9','INPUT')

while True:
	if power_overrun.get_value()==False:
		print "Power overrun !";
		sleep(1)

