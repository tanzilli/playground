#!/usr/bin/python
#Factory test for Daisy-5 and Daisy-11 boards

import ablid
import time
 
daisy11_connector = 'D2'
daisy5_connector = 'D5'
 
# Create a list istances for all the leds
led = [
	ablib.Daisy11(daisy11_connector,'L1'),
	ablib.Daisy11(daisy11_connector,'L2'),
	ablib.Daisy11(daisy11_connector,'L3'),
	ablib.Daisy11(daisy11_connector,'L4'),
	ablib.Daisy11(daisy11_connector,'L5'),
	ablib.Daisy11(daisy11_connector,'L6'),
	ablib.Daisy11(daisy11_connector,'L7'),
	ablib.Daisy11(daisy11_connector,'L8')
	]

# Create a list istances for all buttons
button = [
	ablib.Daisy5(daisy5_connector,'P1'),
	ablib.Daisy5(daisy5_connector,'P2'),
	ablib.Daisy5(daisy5_connector,'P3'),
	ablib.Daisy5(daisy5_connector,'P4'),
	ablib.Daisy5(daisy5_connector,'P5'),
	ablib.Daisy5(daisy5_connector,'P6'),
	ablib.Daisy5(daisy5_connector,'P7'),
	ablib.Daisy5(daisy5_connector,'P8')
	]
 
while True:                 
	for i in range (0,8):  
		if button[i].pressed():
			led[i].on() 
		else:
			led[i].off() 

