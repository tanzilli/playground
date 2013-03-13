#!/usr/bin/python
#Factory test for Daisy-10 boards
#RS422/RS485

import ablib
import time
import serial

#0x27 for PCF8474 T
#0x3F for PCF8474 AT
LCD_ADDRESS = 0x27

lcd = ablib.Daisy24(0,LCD_ADDRESS)
lcd.backlighton()
lcd.clear()
lcd.putstring("TEST Daisy-10")

#RS422 on D1 (/dev/ttyS2)
rs422 = serial.Serial(
	port='/dev/ttyS2', 
	baudrate=9600, 
	timeout=0.5,
	parity=serial.PARITY_NONE,
	stopbits=serial.STOPBITS_ONE,
	bytesize=serial.EIGHTBITS
)  

#RS485 on D3 (/dev/ttyS1)
rs485 = serial.Serial(
	port='/dev/ttyS1', 
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

while True:
	if lcd.pressed(0)==True:
		lcd.clear()
		rs422.flushInput()
		rs485.flushInput()
		sample.flushInput()

		lcd.setcurpos(0,0)
		lcd.putstring("RS422  TX -> RX")

		err=0
		for i in range(0,256):
			lcd.setcurpos(7,1)
			lcd.putstring("%3d" % i)
			rs422.write(chr(i))		

			rx_token = sample.read(1)
			if len(rx_token)==0:
				print "timeout"
				err=err+1
				lcd.setcurpos(0,1)
				lcd.putstring("KO:%3d" % err)
			else:
				lcd.setcurpos(13,1)
				lcd.putstring("%3d" % ord(rx_token))
				if rx_token==chr(i):
					print "ricevuto"
				else: 
					err=err+1
					lcd.setcurpos(0,1)
					lcd.putstring("KO:%3d" % err)
					print "Errore"

	if lcd.pressed(1)==True:
		lcd.clear()
		rs422.flushInput()
		rs485.flushInput()
		sample.flushInput()

		lcd.setcurpos(0,0)
		lcd.putstring("RS422  RX <- TX")

		err=0
		for i in range(0,256):
			lcd.setcurpos(7,1)
			lcd.putstring("%3d" % i)
			sample.write(chr(i))		

			rx_token = rs422.read(1)
			if len(rx_token)==0:
				print "timeout"
				err=err+1
				lcd.setcurpos(0,1)
				lcd.putstring("KO:%3d" % err)
			else:
				lcd.setcurpos(13,1)
				lcd.putstring("%3d" % ord(rx_token))
				if rx_token==chr(i):
					print "ricevuto"
				else: 
					err=err+1
					lcd.setcurpos(0,1)
					lcd.putstring("KO:%3d" % err)
					print "Errore"
	
	
	
