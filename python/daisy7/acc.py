#!/usr/bin/python

#ACCELEROMETER
#Read the internal register

import smbus

lis331dlh_register = {
	'WHO_AM_I'			:	0x0F,
	'CTRL_REG1'			:	0x20,
	'CTRL_REG2'			:	0x21,	
	'CTRL_REG3'			:	0x22,	
	'CTRL_REG4'			:	0x23,
	'CTRL_REG5'			:	0x24,	
	'HP_FILTER_RESET'	:	0x25,
	'REFERENCE'			:	0x26,
	'STATUS_REG'		:   0x27,
	'OUT_X_L'			:	0x28,	
	'OUT_X_H'			:	0x29,	
	'OUT_Y_L'			:	0x2A,	
	'OUT_Y_H'			:	0x2B,	
	'OUT_Z_L'			:	0x2C,	
	'OUT_Z_H'			:	0x2D,
	'INT1_CFG'			:	0x30,
	'INT1_SRC'			:	0x31,
	'INT1_THS'			:	0x32,
	'INT1_DURATION'		:	0x33,
	'INT2_CFG'			:	0x34,
	'INT2_SRC' 			:	0x35,
	'INT1_THS'			:	0x36,
	'INT2_DURATION'		:	0x37,
}

i2c_bus=smbus.SMBus(0)
i2c_address=0x18

for key in sorted(lis331dlh_register.keys()):
	i2c_bus.write_byte(i2c_address,lis331dlh_register[key])		
	print "%s=0x%02X" % (key,i2c_bus.read_byte(i2c_address))



