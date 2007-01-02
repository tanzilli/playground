#!/usr/bin/python

# Send a SMS
import serial
import time

# DAISY-13 plugged on Terra D10 connector
serialport = "/dev/ttyS4"


# Insert here the destination number
send_to = "+393460624344"
message = "Hello World !"

ser = serial.Serial(
	port=serialport, 
	baudrate=115200, 
	timeout=1,
	parity=serial.PARITY_NONE,
	stopbits=serial.STOPBITS_ONE,
	bytesize=serial.EIGHTBITS
)
ser.flushOutput()
ser.flushInput()

ser.write("AT\r")
print ser.readlines()

ser.write("AT\r")
print ser.readlines()

ser.write("ATH\r")
print ser.readlines()
 
ser.write("AT+CMGF=1\r")
print ser.readlines()

ser.write("AT+CMGS=" + "\"" + send_to + "\"" + "\r")
time.sleep(0.5);
ser.write(message + "\x1a")
time.sleep(1);
print ser.readlines()

ser.close()
