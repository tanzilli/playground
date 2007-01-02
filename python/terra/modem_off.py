#!/usr/bin/python
import time
import ablib
 
print "Modem OFF"
 
quectel_power = ablib.Pin('W','10','low')
quectel_power_key = ablib.Pin('E','10','low')

