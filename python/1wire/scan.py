#!/usr/bin/python
import time
import fox
 
print "Scan for the available thermal sensors"
 
for device in fox.w1buslist():
	print "Sensor ID = " + device
