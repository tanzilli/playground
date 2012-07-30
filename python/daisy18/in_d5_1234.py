import ablib
import time

# Tests the first bits in input for Daisy18
# Daisy18 module wired on D2 connector

In1 = ablib.Daisy18('D5','first','I1')
In2 = ablib.Daisy18('D5','first','I2')
In3 = ablib.Daisy18('D5','first','I3')
In4 = ablib.Daisy18('D5','first','I4')
 
print "Start Test"
 
while True:
	if In1.activated():
		print "In 1 Activated"
		time.sleep(0.5)
	if In2.activated():
		print "In 2 Activated"
		time.sleep(0.5)
	if In3.activated():
		print "In 3 Activated"
		time.sleep(0.5)
	if In4.activated():
		print "In 4 Activated"
		time.sleep(0.5)
