import ablib
import time
 
print "Pressing button"
print "Type ctrl-C to exit"
 
led = ablib.Pin('J7','3','low')
button = ablib.Pin('J7','5','in')
 
while True:
	if button.get_value()==0:
		led.on()
	else:
		led.off()

