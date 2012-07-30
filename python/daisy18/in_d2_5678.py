import ablib
import time

# Tests the second bits in input for Daisy18
# Daisy18 module wired on D2 connector

In5 = ablib.Daisy18('D2','second','I1')
In6 = ablib.Daisy18('D2','second','I2')
In7 = ablib.Daisy18('D2','second','I3')
In8 = ablib.Daisy18('D2','second','I4')
 
print "Start Test"
 
while True:
	if In5.activated():
		print "In 5 Activated"
		time.sleep(0.5)
	if In6.activated():
		print "In 6 Activated"
		time.sleep(0.5)
	if In7.activated():
		print "In 7 Activated"
		time.sleep(0.5)
	if In8.activated():
		print "In 8 Activated"
		time.sleep(0.5)
