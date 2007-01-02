from ablib import Pin
from time import sleep
 
print "Blinking led"
print "Type ctrl-C to exit"
 
led = Pin('N20','OUTPUT')

while True:
	sleep(0.2)
	led.on()
	sleep(0.2)
	led.off()

