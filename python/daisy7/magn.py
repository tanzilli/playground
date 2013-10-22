#!/usr/bin/python

#MAGNETOMETER (COMPASS)
#Read the internal registers

import smbus

hmc5883l_register = {
	'CONF_REG_A'		:	0x00,
	'CONF_REG_B'		:	0x01,
	'MODE_REG'			:	0x02,	
	'OUT_X_H'			:	0x03,	
	'OUT_X_L'			:	0x04,
	'OUT_Z_H'			:	0x05,	
	'OUT_Z_L'			:	0x06,
	'OUT_Y_H'			:	0x07,	
	'OUT_Y_L'			:	0x08,
	'STATUS_REG'		:   0x09,
	'ID_REG_A'			:	0x0A,
	'ID_REG_B'			:	0x0B,
	'ID_REG_C'			:	0x0C,
}

i2c_bus=smbus.SMBus(0)
i2c_address=0x1E

print "Registers read from the magnetometer chip"

for key in sorted(hmc5883l_register.keys()):
	i2c_bus.write_byte(i2c_address,hmc5883l_register[key])		
	print "%s=0x%02X" % (key,i2c_bus.read_byte(i2c_address))



