# ssc03a.py
#
# Class abstraction for the Pololu SSC03A servo controler
#
# (C) 2012 Sergio Tanzilli <tanzilli@acmesystems.it>
# (C) 2012 Acme Systems srl (http://www.acmesystems.it)
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.

try:
	import serial
except:
	print "Please install pySerial module"
	quit()

import time

serial_ports = {
	'D1' :  '/dev/ttyS2',
	'D2' :  '/dev/ttyS5',
	'D3' :  '/dev/ttyS1',
	'D5' :  '/dev/ttyS6',
	'D6' :  '/dev/ttyS4',
	'D8' :  '/dev/ttyS3'
} 

class SSC03A():
	serid=-1
	centerpos=-1
	offsetpos=-1

	def __init__(self,whereisit="/dev/ttyS3"):
		if (whereisit.find("/dev/")<>-1):
			serialdevice=whereisit
		else:
			serialdevice=serial_ports[whereisit]

		self.serid = serial.Serial(
			port=serialdevice,
			baudrate=2400, 
			timeout=1,
			parity=serial.PARITY_NONE,
			stopbits=serial.STOPBITS_ONE,
			bytesize=serial.EIGHTBITS,
			xonxoff=False, 
			rtscts=False
		)  
		return

	def sendpos(self,servoid,value):
		self.serid.write(chr(0xFF) + chr(servoid+0x08) + chr(value))
		time.sleep(0.5)
		
	def setcenter(self,value):
		self.centerpos=value
		return

	def setoffset(self,value):
		self.offsetpos=value
		return

	def setpos(self,value):
		return
	

servo0=SSC03A("D8")
servo0.sendpos(0,100)
servo0.sendpos(0,140)
 


