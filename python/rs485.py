#!/usr/bin/python
import serial,fcntl, struct
 
ser = serial.Serial(
	port='/dev/ttyS2', 
	baudrate=9600, 
	timeout=1,
	parity=serial.PARITY_NONE,
	stopbits=serial.STOPBITS_ONE,
	bytesize=serial.EIGHTBITS
)  
 
fd=ser.fileno()
serial_rs485 = struct.pack('hhhhhhhh', 1, 0, 0, 0, 0, 0, 0, 0)
fcntl.ioctl(fd,0x542F,serial_rs485)
 
 
ser.write("A")		# Send a "A" char to the serial port
s = ser.read(1)         # Wait for a char
print s
ser.close()
