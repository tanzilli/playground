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

print "Coordinates from GPS receiver (type Ctrl-C to exit)"

while True:
	#Read a line from the GPS chip
	NMEA_line = ser.readline()

	#Split the fields in NMEA line
	values=NMEA_line.split(",")

	#Select just the GGA message line with GPS quality indicator = 1
	#(see the GPS datasheet)
	if values[0]=="$GPGGA" and values[6]=="1":
		print " Latidute:  %s %s" % (values[2],values[3])
		print "Longitude: %s %s" % (values[4],values[5])
	

