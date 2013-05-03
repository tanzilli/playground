#!/usr/bin/python
import time
import ablib
 
# Create a list of led istances on Daisy-11

connector_buttons="D11"
connector_leds="D12"

button = [
	ablib.Daisy5(connector_buttons,'P1'),
	ablib.Daisy5(connector_buttons,'P2'),
	ablib.Daisy5(connector_buttons,'P3'),
	ablib.Daisy5(connector_buttons,'P4'),
	ablib.Daisy5(connector_buttons,'P5'),
	ablib.Daisy5(connector_buttons,'P6'),
	ablib.Daisy5(connector_buttons,'P7'),
	ablib.Daisy5(connector_buttons,'P8'),
]

led = [
	ablib.Daisy11(connector_leds,'L1'),
	ablib.Daisy11(connector_leds,'L2'),
	ablib.Daisy11(connector_leds,'L3'),
	ablib.Daisy11(connector_leds,'L4'),
	ablib.Daisy11(connector_leds,'L5'),
	ablib.Daisy11(connector_leds,'L6'),
	ablib.Daisy11(connector_leds,'L7'),
	ablib.Daisy11(connector_leds,'L8'),
]
 


# Forever loop
while True:
	# Scan each button and turn the relative led
	for i in range (0,8):      
		if button[i].get(): 
			led[i].on() 
		else: 
			led[i].off()
 

