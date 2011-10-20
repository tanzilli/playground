import fox
import time
 
# Create a list istances for all the leds
# on a Daisy11 module wired on D2 connector
 
led = [
	fox.Daisy11('D2','L1'),
	fox.Daisy11('D2','L2'),
	fox.Daisy11('D2','L3'),
	fox.Daisy11('D2','L4'),
	fox.Daisy11('D2','L5'),
	fox.Daisy11('D2','L6'),
	fox.Daisy11('D2','L7'),
	fox.Daisy11('D2','L8')
	]
 
while True:                        # Forever loop
	for i in range (0,8):      # Scan and turn on all the leds 
		led[i].on()        # each 100 mS
		time.sleep(0.1)
 
	for i in range (0,8):      # Scan and turn off all the leds 
		led[i].off()       # each 100 mS
		time.sleep(0.1)
