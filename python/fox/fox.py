# fox.py
#
# Python collection of funcions that allows to easily manage the FOX 
# Board G20 I/O lines and Daisy building modules.
#
# (C) 2011 Sergio Tanzilli <tanzilli@acmesystems.it>
# (C) 2011 Acme Systems srl (http://www.acmesystems.it)
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.

import os.path
		
# Connectors pin assignments
# 'pin name', 'kernel id'  # pin description

J7_kernel_ids = {
	'3'  :  82,
	'4'  :  83,
	'5'  :  80,
	'6'  :  81,
	'7'  :  66,
	'8'  :  67,
	'9'  :  64,
	'10' :  65,
	'11' : 110,
	'12' : 111,
	'13' : 108,
	'14' : 109,
	'15' : 105,
	'16' : 106,
	'17' : 103,
	'18' : 104,
	'19' : 101,
	'20' : 102,
	'21' :  73,
	'22' :  72,
	'31' :  87,
	'32' :  86,
	'33' :  89,
	'34' :  88,
	'35' :  60,
	'36' :  59,
	'37' :  58,
	'38' :  57,
}

J6_kernel_ids = {
	'3'  :  92,
	'4'  :  71,
	'5'  :  70,
	'6'  :  93,
	'7'  :  90,
	'8'  :  69,
	'9'  :  68,
	'10' :  91,
	'13' :  75,
	'14' :  74,
	'15' :  77,
	'16' :  76,
	'17' :  85,
	'18' :  84,
	'19' :  95,
	'20' :  94,
	'21' :  63,
	'22' :  62,
	'24' :  38,
	'25' :  39,
	'26' :  41,
	'27' :  99,
	'28' :  98,
	'29' :  97,
	'30' :  96,
	'31' :  56,
	'32' :  55,
	'36' :  42,
	'37' :  54,
	'38' :  43,
}


D1_kernel_ids = {
	'1' :  0,  #3V3
	'2' :  70, #PB6
	'3' :  71, #PB7
	'4' :  92, #PB28
	'5' :  93, #PB29
	'6' :   0, #N.C.
	'7' :  55, #PA23
	'8' :  56, #PA24
	'9' :   0, #5V0
	'10':   0, #GND
}

D2_kernel_ids = {
	'1' :   0, #3V3
	'2' :  63, #PA31
	'3' :  62, #PA30
	'4' :  61, #PA29
	'5' :  60, #PA28
	'6' :  59, #PA27
	'7' :  58, #PA26
	'8' :  57, #PA25
	'9' :  94, #PB30
	'10':   0, #GND
}

D3_kernel_ids = {
	'1' :  0,  #3V3
	'2' :  68, #PB4
	'3' :  69, #PB5
	'4' :  90, #PB26
	'5' :  91, #PB27
	'6' :  86, #PB22
	'7' :  88, #PB24
	'8' :  89, #PB25
	'9' :  87, #PB23
	'10':  0,  #GND
}

D4_kernel_ids = {
	'1' :  0,  #3V3
	'2' :  0, #AVDD
	'3' :  0, #VREF
	'4' :  0, #AGND
	'5' :  96, #PC0
	'6' :  97, #PC1
	'7' :  98, #PC2
	'8' :  99, #PC3
	'9' :  0,  #5V0
	'10':  0,  #GND
}


D5_kernel_ids = {
	'1' :  0,  #3V3
	'2' :  76, #PB12
	'3' :  77, #PB13
	'4' :  80, #PB16
	'5' :  81, #PB17
	'6' :  82, #PB18
	'7' :  83, #PB19
	'8' :  84, #PB20
	'9' :  85, #PB21
	'10':  0,  #GND
}

D6_kernel_ids = {
	'1' :  0,  #3V3
	'2' :  74, #PB10
	'3' :  75, #PB11
	'4' : 104, #PC8
	'5' : 106, #PC10
	'6' :  95, #PB31
	'7' :  55, #PA23
	'8' :  56, #PA24
	'9' :   0, #5V0
	'10':   0, #GND
}

D7_kernel_ids = {
	'1' :  0,  #3V3
	'2' :  65, #PB1
	'3' :  64, #PB0
	'4' :  66, #PB2
	'5' :  67, #PB3
	'6' : 101, #PC5
	'7' : 100, #PC4
	'8' :  99, #PC3
	'9' :   0, #5V0
	'10':   0, #GND
}

D8_kernel_ids = {
	'1' :  0,  #3V3
	'2' :  72, #PB8
	'3' :  73, #PB9
	'4' :   0, #N.C.
	'5' :   0, #N.C.
	'6' :   0, #N.C.
	'7' :  55, #PA23
	'8' :  56, #PA24
	'9' :   0, #5V0
	'10':   0, #GND
}

# Kernel IDs descriptors for each connector

connectors = {
	'J6' :  J6_kernel_ids,
	'J7' :  J7_kernel_ids,
	'D1' :  D1_kernel_ids,
	'D2' :  D2_kernel_ids,
	'D3' :  D3_kernel_ids,
	'D4' :  D4_kernel_ids,
	'D5' :  D5_kernel_ids,
	'D6' :  D6_kernel_ids,
	'D7' :  D7_kernel_ids,
	'D8' :  D8_kernel_ids,
}

def get_kernel_id(connector_name,pin_number):
	return connectors[connector_name][pin_number]

def export(kernel_id):
	iopath='/sys/class/gpio/gpio' + str(kernel_id)
	if not os.path.exists(iopath): 
		f = open('/sys/class/gpio/export','w')
		f.write(str(kernel_id))
		f.close()

def direction(kernel_id,direct):
	iopath='/sys/class/gpio/gpio' + str(kernel_id)
	if os.path.exists(iopath): 
		f = open(iopath + '/direction','w')
		f.write(direct)
		f.close()

def set_value(kernel_id,value):
	iopath='/sys/class/gpio/gpio' + str(kernel_id)
	if os.path.exists(iopath): 
		f = open(iopath + '/value','w')
		f.write(str(value))
		f.close()

def get_value(kernel_id):
	if kernel_id<>-1:
		iopath='/sys/class/gpio/gpio' + str(kernel_id)
		if os.path.exists(iopath): 
			f = open(iopath + '/value','r')
			a=f.read()
			f.close()
			return int(a)

class Pin():
	"""
	FOX pins related class
	"""
	kernel_id=-1

	def __init__(self,connector_id,pin_name,direct):
		self.kernel_id=get_kernel_id(connector_id,pin_name)
		export(self.kernel_id)
		direction(self.kernel_id,direct)

	def on(self):
		set_value(self.kernel_id,1)
		
	def off(self):
		set_value(self.kernel_id,0)

	def set_value(self,value):
		return set_value(self.kernel_id,value)

	def get_value(self):
		return get_value(self.kernel_id)

class Daisy4():

	"""
	DAISY-4 (Relay module) related class
	http://www.acmesystems.it/?id=daisy_4_one_relay
	"""
	kernel_id=-1

	dips = {
		'DIP1' :  '2',
		'DIP2' :  '3',
		'DIP3' :  '4',
		'DIP4' :  '5',
		'DIP5' :  '6',
		'DIP6' :  '7',
		'DIP7' :  '8',
		'DIP8' :  '9',
	}

	def __init__(self,connector_id,dip_id):
		pin=self.dips[dip_id]
		self.kernel_id = get_kernel_id(connector_id,pin)

		if (self.kernel_id!=0):
			export(self.kernel_id)
			direction(self.kernel_id,'low')


	def on(self):
		if (self.kernel_id!=0):
			set_value(self.kernel_id,1)
		else:
			pass

		
	def off(self):
		if (self.kernel_id!=0):
			set_value(self.kernel_id,0)
		else:
			pass
	
	
	
class Daisy5():

	"""
	DAISY-5 (8 pushbuttons) related class
	http://www.acmesystems.it/?id=daisy_5_push_buttons
	"""
	kernel_id=-1

	buttons = {
		'P1' :  '2',
		'P2' :  '3',
		'P3' :  '4',
		'P4' :  '5',
		'P5' :  '6',
		'P6' :  '7',
		'P7' :  '8',
		'P8' :  '9',
	}

	def __init__(self,connector_id,button_id):
		pin=self.buttons[button_id]
		self.kernel_id = get_kernel_id(connector_id,pin)

		if (self.kernel_id!=0):
			export(self.kernel_id)
			direction(self.kernel_id,'in')

	def pressed(self):
		if self.kernel_id<>-1:
			iopath='/sys/class/gpio/gpio' + str(self.kernel_id)
			if os.path.exists(iopath): 
				f = open(iopath + '/value','r')
				a=f.read()
				f.close()
				if int(a)==0:
					return False
				else:
					return True
		return False

	def on(self):
		if self.handler_on!=0: 
			self.handler_on()

	def off(self):
		if self.handler_off!=0: 
			self.handler_off()

class Daisy11():

	"""
	DAISY-11 (8 led) related class
	http://www.acmesystems.it/?id=daisy_11_leds
	"""

	kernel_id=-1

	leds = {
		'L1' :  '2',
		'L2' :  '3',
		'L3' :  '4',
		'L4' :  '5',
		'L5' :  '6',
		'L6' :  '7',
		'L7' :  '8',
		'L8' :  '9',
	}

	def __init__(self,connector_id,led_id):
		pin=self.leds[led_id]
		self.kernel_id = get_kernel_id(connector_id,pin)

		if (self.kernel_id!=0):
			export(self.kernel_id)
			direction(self.kernel_id,'low')


	def on(self):
		if (self.kernel_id!=0):
			set_value(self.kernel_id,1)
		else:
			pass

		
	def off(self):
		if (self.kernel_id!=0):
			set_value(self.kernel_id,0)
		else:
			pass

	def get(self):
		if get_value(self.kernel_id):
			return True
		else:
			return False

class Daisy19():

	"""
	DAISY-19 (4 mosfet output) related class
	http://www.acmesystems.it/?id=daisy19_4_mosfet_output	
	"""

	kernel_id=-1

	outputs_first = {
		'O1' :  '2',
		'O2' :  '3',
		'O3' :  '4',
		'O4' :  '5',
	}

	outputs_second = {
		'O1' :  '6',
		'O2' :  '7',
		'O3' :  '8',
		'O4' :  '9',
	}

	def __init__(self,connector_id,position,output_id):
		if (position=="first"): 
			pin=self.outputs_first[output_id]
		else:
			pin=self.outputs_second[output_id]
			
		self.kernel_id = get_kernel_id(connector_id,pin)

		if (self.kernel_id!=0):
			export(self.kernel_id)
			direction(self.kernel_id,'low')


	def on(self):
		if (self.kernel_id!=0):
			set_value(self.kernel_id,1)
		else:
			pass

	def off(self):
		if (self.kernel_id!=0):
			set_value(self.kernel_id,0)
		else:
			pass

	def get(self):
		if get_value(self.kernel_id):
			return True
		else:
			return False


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

class DS28EA00():

	sensor_path=""

	def __init__(self,w1Id):
		if not os.path.exists(w1path): 
			print "1-wire bus not found"
			return

		self.sensor_path = os.path.join(w1path,"42-" + w1Id)

		if not os.path.exists(self.sensor_path): 
			print "Sensor %s not found" % (w1Id)
			return

#		print self.sensor_path

	def getTemp(self):

		f = open(self.sensor_path + '/therm','r')
		tString=f.read()
		f.close()

		if tString.find("NO")>=0:
			print "Wrong CRC"
			return
			
		p=tString.find("t=")
		return float(tString[p+2:-1])

