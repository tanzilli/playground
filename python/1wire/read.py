#!/usr/bin/python
import time
import fox
 
sensor = fox.DS18B20("0000028fa89c")
 
print "Temp=%.2f C" % (sensor.getTemp())

