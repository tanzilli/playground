# Send a SMS using a Daisy13 module wired on D1 connector
# or a FOXGM2 board

import serial
import time

# Insert here the destination number
send_to = "+393460624344"
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
