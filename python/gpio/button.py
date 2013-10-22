from ablib import Pin
from time import sleep
 
led = Pin('W9','OUTPUT')
button = Pin('W15','INPUT')
 
while True:
	if button.digitalRead()==0:
		led.on()
	else:
		led.off()

