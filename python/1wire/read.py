from ablib import DS18B20
 
sensor = DS18B20("0000028fa89c")
print "Temp=%.2f C" % (sensor.getTemp())

