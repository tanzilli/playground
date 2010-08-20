#!/usr/bin/python
#E' solo una prova

import daisy
import time
 
myled = daisy.Daisy11('D2','L2')
 
while True:
	myled.on()
	time.sleep(1)
	myled.off()
	time.sleep(1)
