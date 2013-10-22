#!/usr/bin/python
#Factory test for Daisy-20 boards
import ablib
import time
import os

#0x27 for PCF8474 T
#0x3F for PCF8474 AT
LCD_ADDRESS = 0x3F
VREF=3.24
volt_per_point=VREF/2**10
path="/sys/bus/platform/devices/at91_adc/"

lcd = ablib.Daisy24(0,LCD_ADDRESS)

lcd.backlighton()
lcd.setcurpos(6,0)
lcd.putstring("TEST")
lcd.setcurpos(6,1)
lcd.putstring("D-20")

#if lcd.pressed(0):

ch=0
while True:
	fd = open(path + "chan" + str(ch),"r")
	sample = fd.read()
	print "Channel %d = %.2f volt" % (ch,int(sample)*volt_per_point)
	if ch==0:
		lcd.setcurpos(0,0)
		lcd.putstring("%.2f" % (int(sample)*volt_per_point))
	if ch==1:
		lcd.setcurpos(12,0)
		lcd.putstring("%.2f" % (int(sample)*volt_per_point))
	if ch==2:
		lcd.setcurpos(0,1)
		lcd.putstring("%.2f" % (int(sample)*volt_per_point))
	if ch==3:
		lcd.setcurpos(12,1)
		lcd.putstring("%.2f" % (int(sample)*volt_per_point))
	fd.close()
	ch+=1
	if ch==4: 
		ch=0
		print "-------"

	if lcd.pressed(0) and lcd.pressed(1):
		lcd.clear()
		lcd.putstring("BYE BYE ...")
		time.sleep(1)
		lcd.backlightoff()
		print "Shuthdown"
		os.system("shutdown -h now")
		

