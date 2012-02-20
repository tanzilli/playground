#!/usr/bin/python
import serial

#Wire the DAISY-15 on D8
display_port = "/dev/ttyS3"
 
# Open the serial port on J16
ser = serial.Serial(
	port=display_port, 
	baudrate=9600, 
	timeout=1,
	parity=serial.PARITY_NONE,
	stopbits=serial.STOPBITS_ONE,
	bytesize=serial.EIGHTBITS
)  
 
print ser.portstr	# Check which port was really used
ser.write("U")		# Autobaud char
s = ser.read(1)		# Wait for a reply
ser.write("E")		# Clear screen
s = ser.read(1)
ser.close()
