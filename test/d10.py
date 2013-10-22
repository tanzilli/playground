#!/usr/bin/python
#Factory test for Daisy-10 boards
#RS422/RS485

import ablib
import time
import serial
import fcntl
import struct

#0x27 for PCF8474 T
#0x3F for PCF8474 AT
LCD_ADDRESS = 0x27


def rs422_tx_rx(lcd): 
	#RS422 on D1 (/dev/ttyS2)
	rs422 = serial.Serial(
		port='/dev/ttyS2', 
		baudrate=9600, 
		timeout=0.5,
		parity=serial.PARITY_NONE,
		stopbits=serial.STOPBITS_ONE,
		bytesize=serial.EIGHTBITS
	)  

	#Sample on D6 (/dev/ttyS4)
	sample = serial.Serial(
		port='/dev/ttyS4', 
		baudrate=9600, 
		timeout=0.5,
		parity=serial.PARITY_NONE,
		stopbits=serial.STOPBITS_ONE,
		bytesize=serial.EIGHTBITS
	)  

	lcd.clear()
	rs422.flushInput()
	sample.flushInput()

	lcd.setcurpos(0,0)
	lcd.putstring("RS422  TX -> RX")

	err=0
	for i in range(0,256):
		if err>10:
			rs422.close()
			sample.close()
			return
		lcd.setcurpos(7,1)
		lcd.putstring("%3d" % i)
		rs422.write(chr(i))		

		rx_token = sample.read(1)
		if len(rx_token)==0:
			#print "Timeout"
			err=err+1
			lcd.setcurpos(0,1)
			lcd.putstring("KO:%3d" % err)
		else:
			lcd.setcurpos(13,1)
			lcd.putstring("%3d" % ord(rx_token))
			if rx_token==chr(i):
				#print "Rx ok"
				pass
			else: 
				err=err+1
				lcd.setcurpos(0,1)
				lcd.putstring("KO:%3d" % err)
				#print "Rx error"
				pass

	rs422.close()
	sample.close()
	return

def rs422_rx_tx(lcd): 
	#RS422 on D1 (/dev/ttyS2)
	rs422 = serial.Serial(
		port='/dev/ttyS2', 
		baudrate=9600, 
		timeout=0.5,
		parity=serial.PARITY_NONE,
		stopbits=serial.STOPBITS_ONE,
		bytesize=serial.EIGHTBITS
	)  

	#Sample on D6 (/dev/ttyS4)
	sample = serial.Serial(
		port='/dev/ttyS4', 
		baudrate=9600, 
		timeout=0.5,
		parity=serial.PARITY_NONE,
		stopbits=serial.STOPBITS_ONE,
		bytesize=serial.EIGHTBITS
	)  

	lcd.clear()
	rs422.flushInput()
	sample.flushInput()

	lcd.setcurpos(0,0)
	lcd.putstring("RS422  RX <- TX")

	err=0
	for i in range(0,256):
		if err>10:
			break
		lcd.setcurpos(7,1)
		lcd.putstring("%3d" % i)
		sample.write(chr(i))		

		rx_token = rs422.read(1)
		if len(rx_token)==0:
			#print "Timeout"
			err=err+1
			lcd.setcurpos(0,1)
			lcd.putstring("KO:%3d" % err)
		else:
			lcd.setcurpos(13,1)
			lcd.putstring("%3d" % ord(rx_token))
			if rx_token==chr(i):
				#print "Rx ok"
				pass
			else: 
				err=err+1
				lcd.setcurpos(0,1)
				lcd.putstring("KO:%3d" % err)
				#print "Rx error"
				pass

	rs422.close()
	sample.close()
	return

def rs485_tx_rx(lcd): 
	#RS485 on D3 (/dev/ttyS1)
	rs485 = serial.Serial(
		port='/dev/ttyS1', 
		baudrate=9600, 
		rtscts=True,
		timeout=0.5,
		parity=serial.PARITY_NONE,
		stopbits=serial.STOPBITS_ONE,
		bytesize=serial.EIGHTBITS
	)  

	fd=rs485.fileno()
	serial_rs485 = struct.pack('hhhhhhhh', 1, 0, 0, 0, 0, 0, 0, 0)
	fcntl.ioctl(fd,0x542F,serial_rs485)

	#Sample on D6 (/dev/ttyS4)
	sample = serial.Serial(
		port='/dev/ttyS4', 
		baudrate=9600, 
		timeout=0.5,
		parity=serial.PARITY_NONE,
		stopbits=serial.STOPBITS_ONE,
		bytesize=serial.EIGHTBITS
	)  
	fd=sample.fileno()
	serial_rs485 = struct.pack('hhhhhhhh', 1, 0, 0, 0, 0, 0, 0, 0)
	fcntl.ioctl(fd,0x542F,serial_rs485)

	lcd.clear()
	rs485.flushInput()
	sample.flushInput()

	lcd.setcurpos(0,0)
	lcd.putstring("RS485  TX -> RX")

	err=0
	for i in range(0,256):
		if err>10:
			rs485.close()
			sample.close()
			return
		lcd.setcurpos(7,1)
		lcd.putstring("%3d" % i)
		rs485.write(chr(i))		

		rx_token = sample.read(1)
		if len(rx_token)==0:
			#print "Timeout"
			err=err+1
			lcd.setcurpos(0,1)
			lcd.putstring("KO:%3d" % err)
		else:
			lcd.setcurpos(13,1)
			lcd.putstring("%3d" % ord(rx_token))
			if rx_token==chr(i):
				#print "Rx ok"
				pass
			else: 
				err=err+1
				lcd.setcurpos(0,1)
				lcd.putstring("KO:%3d" % err)
				#print "Rx error"
				pass

	rs485.close()
	sample.close()
	return

def rs485_rx_tx(lcd): 
	#RS485 on D3 (/dev/ttyS1)
	rs485 = serial.Serial(
		port='/dev/ttyS1', 
		baudrate=9600, 
		rtscts=True,
		timeout=0.5,
		parity=serial.PARITY_NONE,
		stopbits=serial.STOPBITS_ONE,
		bytesize=serial.EIGHTBITS
	)  

	fd=rs485.fileno()
	serial_rs485 = struct.pack('hhhhhhhh', 1, 0, 0, 0, 0, 0, 0, 0)
	fcntl.ioctl(fd,0x542F,serial_rs485)

	#Sample on D6 (/dev/ttyS4)
	sample = serial.Serial(
		port='/dev/ttyS4', 
		baudrate=9600, 
		timeout=0.5,
		parity=serial.PARITY_NONE,
		stopbits=serial.STOPBITS_ONE,
		bytesize=serial.EIGHTBITS
	)  
	fd=sample.fileno()
	serial_rs485 = struct.pack('hhhhhhhh', 1, 0, 0, 0, 0, 0, 0, 0)
	fcntl.ioctl(fd,0x542F,serial_rs485)

	lcd.clear()
	rs485.flushInput()
	sample.flushInput()

	lcd.setcurpos(0,0)
	lcd.putstring("RS485  RX <- TX")

	err=0
	for i in range(0,256):
		if err>10:
			rs485.close()
			sample.close()
			return
		lcd.setcurpos(7,1)
		lcd.putstring("%3d" % i)
		sample.write(chr(i))		

		rx_token = rs485.read(1)
		if len(rx_token)==0:
			#print "Timeout"
			err=err+1
			lcd.setcurpos(0,1)
			lcd.putstring("KO:%3d" % err)
		else:
			lcd.setcurpos(13,1)
			lcd.putstring("%3d" % ord(rx_token))
			if rx_token==chr(i):
				#print "Rx ok"
				pass
			else: 
				err=err+1
				lcd.setcurpos(0,1)
				lcd.putstring("KO:%3d" % err)
				#print "Rx error"
				pass

	rs485.close()
	sample.close()
	return

lcd = ablib.Daisy24(0,LCD_ADDRESS)
lcd.backlighton()
lcd.clear()
lcd.putstring("TEST Daisy-10")



while True:
	if lcd.pressed(0)==True:
		rs422_tx_rx(lcd)

	if lcd.pressed(1)==True:
		rs422_rx_tx(lcd)
	
	if lcd.pressed(3)==True:
		rs485_tx_rx(lcd)

	if lcd.pressed(2)==True:
		rs485_rx_tx(lcd)
	
