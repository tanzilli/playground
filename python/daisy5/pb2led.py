#!/usr/bin/python
import time
import ablib

# Create an istance on Daisy11 class to refer the L1 led
myled = ablib.Daisy11('D2','L1')

# Create an istance on Daisy5 class to refer the P1 push button
mybutton = ablib.Daisy5('D5','P1')

# Never ending loop
while True:
	# If mybutton (P1) is pressed...
	if mybutton.pressed():		
		# ...turn on myled (L1)
		myled.on()
	else:
		# ... if not turn off it
		myled.off()
