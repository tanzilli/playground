#!/usr/bin/python
import time
import daisy
 
# Create a list of led istances
 
led = [
	daisy.Daisy11('D2','L1'),
	daisy.Daisy11('D2','L2'),
	daisy.Daisy11('D2','L3'),
	daisy.Daisy11('D2','L4'),
	daisy.Daisy11('D2','L5'),
	daisy.Daisy11('D2','L6'),
	daisy.Daisy11('D2','L7'),
	daisy.Daisy11('D2','L8'),
	]
 
while True:                        # Forever loop
	for i in range (0,8):      # Scan and turn on all the leds 
		led[i].on()        # each 100 mS
		time.sleep(0.1)
 
	for i in range (0,8):      # Scan and turn off all the leds 
		led[i].off()       # each 100 mS
		time.sleep(0.1)
