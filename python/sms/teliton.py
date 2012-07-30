#!/usr/bin/python
import time
import ablib
 
print "Telit ON/OFF"
 
telitRESET = ablib.Pin('J6','38','low')
telitON = ablib.Pin('J6','37','low')
 
telitON.on()
time.sleep(1)
telitON.off()
