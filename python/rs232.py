#!/usr/bin/python
import serial
 
ser = serial.Serial(
	port='/dev/ttyS1', 
	baudrate=9600, 
	timeout=1,
	parity=serial.PARITY_NONE,
	stopbits=serial.STOPBITS_ONE,
	bytesize=serial.EIGHTBITS
)  
 
ser.write("A")	# Send a "A" char to the serial port
s = ser.read(1)	# Wait for a char
print s
ser.close()
