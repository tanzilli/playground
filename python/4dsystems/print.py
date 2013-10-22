#!/usr/bin/python
import serial,sys,getopt

#Wire the DAISY-15 on D8
display_port = "/dev/ttyS3"
 
try:
	opts, args = getopt.getopt(sys.argv[1:], "x:y:s:b")

except getopt.GetoptError, err:
	# print help information and exit:
	# will print something like "option -a not recognized"
	print str(err) 
	sys.exit(2)
 
x=0
y=0
s=""
clear = False
 
for o, a in opts:
	if o == "-x":
		x = a
	elif o == "-y":
		y = a
	elif o == "-s":
		s = a
	elif o == "-b":
		clear = True
	else:
		assert False, "Unhandled option"
 
# Open the serial port
ser = serial.Serial(
	port=display_port, 
	baudrate=9600, 
	timeout=1,
	parity=serial.PARITY_NONE,
	stopbits=serial.STOPBITS_ONE,
	bytesize=serial.EIGHTBITS
)  
 
# Autobaud char
ser.write("U")		
rtc = ser.read(1)
 
# Clear screen
if clear==True:
	ser.write("E")		
	rtc = ser.read(1)
 
# Send string
ser.write("s%c%c%c%c%c%s%c" % (int(x),int(y),1,0xFF,0xFF,s,0x00))		
rtc = ser.read(1)
 
ser.close()

