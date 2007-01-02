#!/usr/bin/python
import time
import ablib
 
print "Modem ON"
 
quectel_power = ablib.Pin('W','10','high')
quectel_power_key = ablib.Pin('E','10','low')

quectel_power_key.on()
time.sleep(1)
quectel_power_key.off()

