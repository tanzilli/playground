#!/usr/bin/python
import time
import ablib
 
# Create a list of led istances on Daisy-11
# Wire the Daisy-11 board on D2
# Wire the Daisy-5 board on D5

led = [
	ablib.Daisy11('D2','L1'),
	ablib.Daisy11('D2','L2'),
	ablib.Daisy11('D2','L3'),
	ablib.Daisy11('D2','L4'),
	ablib.Daisy11('D2','L5'),
	ablib.Daisy11('D2','L6'),
	ablib.Daisy11('D2','L7'),
	ablib.Daisy11('D2','L8'),
]
 
button = [
	ablib.Daisy5('D5','P1'),
	ablib.Daisy5('D5','P2'),
	ablib.Daisy5('D5','P3'),
	ablib.Daisy5('D5','P4'),
	ablib.Daisy5('D5','P5'),
	ablib.Daisy5('D5','P6'),
	ablib.Daisy5('D5','P7'),
	ablib.Daisy5('D5','P8'),
]

# Forever loop
while True:
	# Scan each button and turn the relative led
	for i in range (0,8):      
		if button[i].pressed(): 
			led[i].on() 
		else: 
			led[i].off()
 

