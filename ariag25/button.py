import ablib
import time
 
print "Press the push-button"
print "or type ctrl-C to exit"
 
led = ablib.Pin('W','9','low')
button = ablib.Pin('W','15','in')
 
while True:
	if button.get_value()==0:
		led.on()
	else:
		led.off()

