#!/usr/bin/python
import time
import ablib
 
print "Scan for the available thermal sensors"
 
for device in ablib.w1buslist():
	print "Sensor ID = " + device
