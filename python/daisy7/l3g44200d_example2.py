import smbus
import sys

l3g4200d_register = {
	'OUT_X_L'			:	0x28,	
	'OUT_X_H'			:	0x29,	
	'OUT_Y_L'			:	0x2A,	
	'OUT_Y_H'			:	0x2B,	
	'OUT_Z_L'			:	0x2C,	
	'OUT_Z_H'			:	0x2D,
}

i2c_bus=smbus.SMBus(0)
i2c_address=0x68

for key in sorted(l3g4200d_register.keys()):
	i2c_bus.write_byte(i2c_address,l3g4200d_register[key])		
	sys.stdout.write ("%s=0x%02X " % (key,i2c_bus.read_byte(i2c_address)))
	print ""



