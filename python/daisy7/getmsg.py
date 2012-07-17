#!/usr/bin/python

import serial
import sys

serialdevice = "/dev/ttyS2"

#Open the serial port 
ser = serial.Serial(
	port=serialdevice, 
	baudrate=115200, 
	timeout=1,
	parity=serial.PARITY_NONE,
	stopbits=serial.STOPBITS_ONE,
	bytesize=serial.EIGHTBITS
)  
ser.flushInput()

print "NMEA messages received from GPS chip (type Ctrl-C to exit)"

while True:
	s = ser.read(1) 
	sys.stdout.write(s)
	sys.stdout.flush()

