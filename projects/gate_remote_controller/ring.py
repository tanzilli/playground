from time import sleep
import ablib
import serial
import re

enabled_numbers = {
	'+393460624304':'Roberto Asquini',
	'+393460624344':'Sergio Tanzilli',
	'+393346203529':'Daniela Necci',
	'+393204460760':'Ennio Negri',
	'+393471018208':'Tiziana Di Laurenzio',
	'+393358724296':'Emanuele Lauria',
	'+393477963828':'Nicola Pye',
	'+393498240562':'Meti Tanzilli',
	'+393897868293':'Andrea Ancora',
}

def getIncomingCall(ser):
	while True:
		for line in ser.readlines():
			print line
			if line.find("+CLIP")>=0:
				m = re.search('"(.+?)"',line)
				if m:
					found = m.group(1)
					return found

def authorized_log(name):
	out_file = open("authorized.log","a")
	out_file.write(name + "\n")
	out_file.close()

def unauthorized_log(number):
	out_file = open("unauthorized.log","a")
	out_file.write(number + "\n")
	out_file.close()
 
ser = serial.Serial(
	port='/dev/ttyS1', 
	baudrate=115200, 
	timeout=1,
	parity=serial.PARITY_NONE,
	stopbits=serial.STOPBITS_ONE,
	bytesize=serial.EIGHTBITS
)

gate = ablib.Daisy8('D11','first','RL1')

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

	ser.write("AT+CLIP=1\r")
	rtc=ser.readlines()
	if "OK\r\n" in rtc:
		break

while True:
	print "Check for incoming calling"
	incoming=getIncomingCall(ser)	
	
	#Look for an enabled number
	try:
		print enabled_numbers[incoming]
		ser.write("ATH\r")
		gate.on()
		sleep(1)
		gate.off()
		authorized_log(enabled_numbers[incoming])
		
	except:	
		print "Unknow---->",incoming
		unauthorized_log(incoming)
		ser.write("ATH\r")
