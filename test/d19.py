#!/usr/bin/python
#Factory test for Daisy-19 boards
import ablib
import time
import os

#0x27 for PCF8474 T
#0x3F for PCF8474 AT
LCD_ADDRESS = 0x27

delay = 0.4

ch1 = ablib.Daisy19("D2","first","CH1")
ch2 = ablib.Daisy19("D2","first","CH2")
ch3 = ablib.Daisy19("D2","first","CH3")
ch4 = ablib.Daisy19("D2","first","CH4")

Inp1 = ablib.Daisy18("D5","first","CH1")
Inp2 = ablib.Daisy18("D5","first","CH2")
Inp3 = ablib.Daisy18("D5","first","CH3")
Inp4 = ablib.Daisy18("D5","first","CH4")


L5=ablib.Daisy11("D2","L5")
L6=ablib.Daisy11("D2","L6")
L7=ablib.Daisy11("D2","L7")
L8=ablib.Daisy11("D2","L8")

lcd = ablib.Daisy24(0,LCD_ADDRESS)
lcd.backlighton()
lcd.setcurpos(6,0)
lcd.putstring("TEST")
lcd.setcurpos(6,1)
lcd.putstring("D-19")

#if lcd.pressed(0):

ch=0
while True:
	if ch==0:
		err=False
		ch1.on()
		L5.on()	
		time.sleep(delay)	
		if Inp1.state()==False:
			err=True
		ch1.off()
		L5.off()	
		time.sleep(delay)	
		if Inp1.state()==True:
			err=True
		if err:
			lcd.setcurpos(0,0)
			lcd.putstring("1 ERR")
		else: 
			lcd.setcurpos(0,0)
			lcd.putstring("1 OK ")

	if ch==1:
		err=False
		ch2.on()
		L6.on()	
		time.sleep(delay)	
		if Inp2.state()==False:
			err=True
		ch2.off()
		L6.off()	
		time.sleep(delay)	
		if Inp2.state()==True:
			err=True
		if err:
			lcd.setcurpos(11,0)
			lcd.putstring("2 ERR")
		else: 
			lcd.setcurpos(11,0)
			lcd.putstring("2 OK ")

	if ch==2:
		err=False
		ch3.on()
		L7.on()	
		time.sleep(delay)	
		if Inp3.state()==False:
			err=True
		ch3.off()
		L7.off()	
		time.sleep(delay)	
		if Inp3.state()==True:
			err=True
		if err:
			lcd.setcurpos(0,1)
			lcd.putstring("3 ERR")
		else: 
			lcd.setcurpos(0,1)
			lcd.putstring("3 OK ")

	if ch==3:
		err=False
		ch4.on()
		L8.on()	
		time.sleep(delay)	
		if Inp4.state()==False:
			err=True
		ch4.off()
		L8.off()	
		time.sleep(delay)	
		if Inp4.state()==True:
			err=True
		if err:
			lcd.setcurpos(11,1)
			lcd.putstring("4 ERR")
		else: 
			lcd.setcurpos(11,1)
			lcd.putstring("4 OK ")


	ch+=1
	if ch==4: 
		ch=0

