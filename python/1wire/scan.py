from ablib import w1buslist
 
print "Scan for the available thermal sensors"
 
for device in w1buslist():
	print "Sensor ID = " + device
