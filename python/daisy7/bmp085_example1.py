import smbus

i2c_bus=smbus.SMBus(0)

# Read the calibration coefficients of BMP085

i2c_address=0x77
for i in range(0xAA,0xBF+1):
	i2c_bus.write_byte(i2c_address,i)		
	print "0x%X = %d " % (i,i2c_bus.read_byte(i2c_address))


