import fox
import time
 
print "Blinking led"
print "Type ctrl-C to exit"
 
led = fox.Pin('J7','3','low')
 
while True:
	time.sleep(0.2)
	led.on()
	time.sleep(0.2)
	led.off()

