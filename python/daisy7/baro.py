#!/usr/bin/python

#BAROMETER (PRESSURE SENSOR)
#Read the internal registers

import smbus

i2c_bus=smbus.SMBus(0)
i2c_address=0x77

print "Registers read from the barometer chip"

for i in range(0xAA,0xBF+1):
	i2c_bus.write_byte(i2c_address,i)		
	print "0x%03d = %d " % (i,i2c_bus.read_byte(i2c_address))


