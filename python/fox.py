# fox.py version 2010_03_11
#
# Collection of Python class to simplify the use of the FOX Board G20
# http://www.acmesystems.it/foxg20
#
# Copyright (C) 2010 Sergio Tanzilli <tanzilli@acmesystems.it>
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.

import os.path

#--------------------------------------------------------------

w1path = "/sys/bus/w1/devices/w1 bus master"

def w1buslist():

		if not os.path.exists(w1path): 
			print "1-wire bus not found"
			print "Check if the 1-wire bus is installed"
			return

		deviceList = os.listdir(w1path)

#		for deviceId in deviceList:
#			print deviceId

		return [deviceId[3:] for deviceId in deviceList if deviceId[0:2]=="28"]

class DS18B20():

	sensor_path=""

	def __init__(self,w1Id):
		if not os.path.exists(w1path): 
			print "1-wire bus not found"
			return

		self.sensor_path = os.path.join(w1path,"28-" + w1Id)

		if not os.path.exists(self.sensor_path): 
			print "Sensor %s not found" % (w1Id)
			return

#		print self.sensor_path

	def getTemp(self):

		f = open(self.sensor_path + '/w1_slave','r')
		tString=f.read()
		f.close()

		if tString.find("NO")>=0:
			print "Wrong CRC"
			return
			
		p=tString.find("t=")
		return float(tString[p+2:-1])/1000
		
		

#--------------------------------------------------------------

class Pin():

	kernelid_table = {
		'J7.3'  :  82,
		'J7.4'  :  83,
		'J7.5'  :  80,
		'J7.6'  :  81,
		'J7.7'  :  66,
		'J7.8'  :  67,
		'J7.9'  :  64,
		'J7.10' :  65,
		'J7.11' : 110,
		'J7.12' : 111,
		'J7.13' : 108,
		'J7.14' : 109,
		'J7.15' : 105,
		'J7.16' : 106,
		'J7.17' : 103,
		'J7.18' : 104,
		'J7.19' : 101,
		'J7.20' : 102,
		'J7.21' :  73,
		'J7.22' :  72,
		'J7.31' :  87,
		'J7.32' :  86,
		'J7.33' :  89,
		'J7.34' :  88,
		'J7.35' :  60,
		'J7.36' :  59,
		'J7.37' :  58,
		'J7.38' :  57,
		'J6.3'  :  92,
		'J6.4'  :  71,
		'J6.5'  :  70,
		'J6.6'  :  93,
		'J6.7'  :  90,
		'J6.8'  :  69,
		'J6.9'  :  68,
		'J6.10' :  91,
		'J6.13' :  75,
		'J6.14' :  74,
		'J6.15' :  77,
		'J6.16' :  76,
		'J6.17' :  85,
		'J6.18' :  84,
		'J6.19' :  95,
		'J6.20' :  94,
		'J6.21' :  63,
		'J6.22' :  62,
		'J6.24' :  38,
		'J6.25' :  39,
		'J6.26' :  41,
		'J6.27' :  99,
		'J6.28' :  98,
		'J6.29' :  97,
		'J6.30' :  96,
		'J6.31' :  56,
		'J6.32' :  55,
		'J6.36' :  42,
		'J6.37' :  54,
		'J6.38' :  43,
	}

	kernelid=-1;

	def __init__(self,pin_name,direction):
		self.kernelid=self.getid(pin_name)
		self.export(self.kernelid)
		self.direction(self.kernelid,direction)

	def getid(self,pin_name):
		return self.kernelid_table[pin_name]
	
	def export(self,kernelid):
		iopath='/sys/class/gpio/gpio' + str(kernelid)
		if not os.path.exists(iopath): 
			f = open('/sys/class/gpio/export','w')
			f.write(str(kernelid))
			f.close()

	def direction(self,kernelid,direction):
		iopath='/sys/class/gpio/gpio' + str(kernelid)
		if os.path.exists(iopath): 
			f = open(iopath + '/direction','w')
			f.write(direction)
			f.close()

	def setValue(self,value):
		iopath='/sys/class/gpio/gpio' + str(self.kernelid)
		if os.path.exists(iopath): 
			f = open(iopath + '/value','w')
			f.write(str(value))
			f.close()

	def getValue(self):
		if self.kernelid<>-1:
			iopath='/sys/class/gpio/gpio' + str(self.kernelid)
			if os.path.exists(iopath): 
				f = open(iopath + '/value','r')
				a=f.read()
				f.close()
				return int(a)
			
	def on(self):
		if self.kernelid<>-1:
			self.setValue(1)

	def off(self):
		if self.kernelid<>-1:
			self.setValue(0)
