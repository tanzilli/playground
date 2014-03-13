from time import sleep
import ablib
import serial
import re

def getIncomingCall(ser):
	while True:
		for line in ser.readlines():
			if line.find("+CLIP")>=0:
				m = re.search('"(.+?)"',line)
				if m:
					found = m.group(1)
					return found
 
ser = serial.Serial(
	port='/dev/ttyS1', 
	baudrate=115200, 
	timeout=1,
	parity=serial.PARITY_NONE,
	stopbits=serial.STOPBITS_ONE,
	bytesize=serial.EIGHTBITS
)

while True:
	#Check if the modem is on
	quectel_STATUS = ablib.Pin('N6','INPUT')

	if quectel_STATUS.get_value()==1:
		print "Modem is ON"
		break
	else: 	
		print "Turn ON the modem"
	 
		quectel_power = ablib.Pin('W10','HIGH')
		quectel_power_key = ablib.Pin('E10','LOW')

		quectel_power_key.on()
		sleep(1)
		quectel_power_key.off()

ser.flushInput()
ser.flushOutput()

print "Wait for a modem reply on serial line"
while True:
	ser.write("ATE0\r")
	rtc=ser.readlines()
	if "OK\r\n" in rtc:
		break

while True:
	print "Check for incoming calling"
	print getIncomingCall(ser)
