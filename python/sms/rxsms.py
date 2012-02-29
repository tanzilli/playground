#!/usr/bin/python
import serial
import time

ser = serial.Serial(
	port='/dev/ttyS1', 
	baudrate=115200, 
	timeout=1,
	parity=serial.PARITY_NONE,
	stopbits=serial.STOPBITS_ONE,
	bytesize=serial.EIGHTBITS
)
ser.flushOutput()
ser.flushInput()

ser.write("ATH\r")
print ser.readlines()
 
ser.write("AT+CMGF=1\r")
print ser.readlines()

ser.write("AT+CNMI=1,2,0,0,0\r")

while True:
	print ser.readlines()

ser.close()

