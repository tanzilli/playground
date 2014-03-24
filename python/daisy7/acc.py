#!/usr/bin/python

#ST LIS331DLH linear accelerometer reading example 
#Read and print the X,Y,Z linear speed any 0.5 sec
#http://acme.systems/DAISY-7

import smbus
import time

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
#converts 16 bit two's compliment reading to signed int
def getSignedNumber(number):
    if number & (1 << 15):
        return number | ~65535
    else:
        return number & 65535


i2c_bus=smbus.SMBus(0)
i2c_address=0x18

print "Read from the accelerometer chip"

#Chip setup

##Chip in Normal mode. Turn on all axis
i2c_bus.write_byte_data(i2c_address,lis331dlh_register['CTRL_REG1'],0x27)


while True:
	i2c_bus.write_byte(i2c_address,lis331dlh_register['STATUS_REG'])		
	status_reg=i2c_bus.read_byte(i2c_address)		
	if (status_reg&0x08)==0:
		continue

	#Read X axis value
	i2c_bus.write_byte(i2c_address,lis331dlh_register['OUT_X_L'])		
	OUT_X_L=i2c_bus.read_byte(i2c_address)		
	i2c_bus.write_byte(i2c_address,lis331dlh_register['OUT_X_H'])		
	OUT_X_H=i2c_bus.read_byte(i2c_address)		
	xValue=getSignedNumber(OUT_X_H<<8 | OUT_X_L)

	#Read Y axis value
	i2c_bus.write_byte(i2c_address,lis331dlh_register['OUT_Y_L'])		
	OUT_Y_L=i2c_bus.read_byte(i2c_address)		
	i2c_bus.write_byte(i2c_address,lis331dlh_register['OUT_Y_H'])		
	OUT_Y_H=i2c_bus.read_byte(i2c_address)		
	yValue=getSignedNumber(OUT_Y_H<<8 | OUT_Y_L)

	#Read Z axis value
	i2c_bus.write_byte(i2c_address,lis331dlh_register['OUT_Z_L'])		
	OUT_Z_L=i2c_bus.read_byte(i2c_address)		
	i2c_bus.write_byte(i2c_address,lis331dlh_register['OUT_Z_H'])		
	OUT_Z_H=i2c_bus.read_byte(i2c_address)		
	zValue=getSignedNumber(OUT_Z_H<<8 | OUT_Z_L)
	
	print "X=%6d Y=%6d Z=%6d" % (xValue,yValue,zValue)
	time.sleep(0.5)


