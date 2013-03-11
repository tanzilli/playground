#!/usr/bin/python
#Factory test for Daisy-18 boards
import ablib
import time
import os

#0x27 for PCF8474 T
#0x3F for PCF8474 AT
LCD_ADDRESS = 0x3F

ch1 = ablib.Daisy19("D2","first","CH1")
ch2 = ablib.Daisy19("D2","first","CH2")
ch3 = ablib.Daisy19("D2","first","CH3")
ch4 = ablib.Daisy19("D2","first","CH4")

lcd = ablib.Daisy24(0,LCD_ADDRESS)
lcd.backlighton()
lcd.setcurpos(6,0)
lcd.putstring("TEST")
lcd.setcurpos(6,1)
lcd.putstring("D-18")

#if lcd.pressed(0):

while True:
	if ch==0:
		ch1.on();
		time.sleep(0.5)	
		ch1.off();
		time.sleep(0.5)	
	if ch==1:
		ch2.on();
		time.sleep(0.5)	
		ch2.off();
		time.sleep(0.5)	
	if ch==2:
		ch3.on();
		time.sleep(0.5)	
		ch3.off();
		time.sleep(0.5)	
	if ch==3:
		ch4.on();
		time.sleep(0.5)	
		ch4.off();
		time.sleep(0.5)	
	ch+=1
	if ch==4: 
		ch=0
		print "-------"

