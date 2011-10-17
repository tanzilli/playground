#!/usr/bin/python 
# Send a SMS example
# Plug the Daisy-13 board on D1

import serial
import time

# Destination number
# Example: +39338123456
send_to = "destination number]"
message = "Hello World !"

ser = serial.Serial(
	port='/dev/ttyS2', 
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

ser.write("AT+CMGS=" + "\"" + send_to + "\"" + "\r")
time.sleep(0.5);
ser.write(message + "\x1a")
time.sleep(1);
print ser.readlines()

ser.close()
