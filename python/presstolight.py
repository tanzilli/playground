#!/usr/bin/python
import time
import daisy
 
# Create a list of led istances on Daisy-11
# Wire the Daisy-11 board on D2
# Wire the Daisy-5 board on D5

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
 
button = [
	daisy.Daisy5('D5','P1'),
	daisy.Daisy5('D5','P2'),
	daisy.Daisy5('D5','P3'),
	daisy.Daisy5('D5','P4'),
	daisy.Daisy5('D5','P5'),
	daisy.Daisy5('D5','P6'),
	daisy.Daisy5('D5','P7'),
	daisy.Daisy5('D5','P8'),
]

# Forever loop
while True:
	# Scan each button and turn the relative led
	for i in range (0,8):      
		if button[i].pressed(): 
			led[i].on() 
		else: 
			led[i].off()
 

