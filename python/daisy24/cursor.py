import ablib
import time

#Check for Daisy-24 address
if ablib.existI2Cdevice(0,0x27):
	i2c_address=0x27
else:
	i2c_address=0x3F

lcd = ablib.Daisy24(0,i2c_address)
lcd.backlighton()

while True:
	for x in range(0,16,12):
		for y in range(2):
			for counter in range (1000+1):
				lcd.setcurpos(x,y)
				lcd.putstring("%4s" % counter)





