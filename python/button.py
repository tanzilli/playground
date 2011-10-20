import fox
import time
 
print "Pressing button"
print "Type ctrl-C to exit"
 
led = fox.Pin('J7','3','low')
button = fox.Pin('J7','5','in')
 
while True:
	if button.get_value()==0:
		led.on()
	else:
		led.off()

