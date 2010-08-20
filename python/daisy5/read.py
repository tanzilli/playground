#!/usr/bin/python

#Read the state of each button on Daisy-5
#when wired on D5 connecor

#http://www.acmesystems.it/DAISY-5

import time
import fox

# Create an istance for each button

P1 = fox.Daisy5('D5','P1')
P2 = fox.Daisy5('D5','P2')
P3 = fox.Daisy5('D5','P3')
P4 = fox.Daisy5('D5','P4')
P5 = fox.Daisy5('D5','P5')
P6 = fox.Daisy5('D5','P6')
P7 = fox.Daisy5('D5','P7')
P8 = fox.Daisy5('D5','P8')

while True:
	if (P1.pressed()):
		print "P1 pressed" 
	if (P2.pressed()):
		print "P2 pressed" 
	if (P3.pressed()):
		print "P3 pressed" 
	if (P4.pressed()):
		print "P4 pressed" 
	if (P5.pressed()):
		print "P5 pressed" 
	if (P6.pressed()):
		print "P6 pressed" 
	if (P7.pressed()):
		print "P7 pressed" 
	if (P8.pressed()):
		print "P8 pressed" 


