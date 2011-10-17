#!/usr/bin/python
import time
import fox
 
print "Blinking led"
print "Type ctrl-C to exit"
 
led = fox.Pin('J7.3','low')
 
while True:
	time.sleep(1)
	led.on()
	time.sleep(1)
	led.off()

