#!/usr/bin/python
import serial
import time

ser = serial.Serial(
	port='/dev/ttyS3', 
	baudrate=4800, 
	timeout=1,
	parity=serial.PARITY_NONE,
	stopbits=serial.STOPBITS_ONE,
	bytesize=serial.EIGHTBITS
)
ser.flushOutput()
ser.flushInput()

while True:
	print ser.readlines()

