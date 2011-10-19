#!/usr/bin/python
import daisy
import time
 
myled = daisy.Daisy11('D2','L1')
 
while True:
	myled.on()
	time.sleep(0.2)
	myled.off()
	time.sleep(0.2)
