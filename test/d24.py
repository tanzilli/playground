import ablib
import time

while True:
	time.sleep(0.2)

	lcd_addr=-1	
	if ablib.existI2Cdevice(0,0x27):
		print "PCF8474T"
		lcd_addr = 0x27
		
	if ablib.existI2Cdevice(0,0x3F):
		print "PCF8474AT"
		lcd_addr = 0x3F
		
	if lcd_addr==-1:
		continue		
	
	try:
		lcd = ablib.Daisy24(0,lcd_addr)
		if lcd_addr==0x27:
			lcd.putstring("Daisy-24 (T)")

		if lcd_addr==0x3F:
			lcd.putstring("Daisy-24 (AT)")

		if lcd.pressed(0):
			lcd.setcurpos(0,1)
			lcd.putstring("Key 0 pressed")
			lcd.backlighton()
			time.sleep(1)
			lcd.backlightoff()

		if lcd.pressed(1):
			lcd.setcurpos(0,1)
			lcd.putstring("Key 1 pressed")
			lcd.backlighton()
			time.sleep(1)
			lcd.backlightoff()

		if lcd.pressed(2):
			lcd.setcurpos(0,1)
			lcd.putstring("Key 2 pressed")
			lcd.backlighton()
			time.sleep(1)
			lcd.backlightoff()

		if lcd.pressed(3):
			lcd.setcurpos(0,1)
			lcd.putstring("Key 3 pressed")
			lcd.backlighton()
			time.sleep(1)
			lcd.backlightoff()

		if  lcd.pressed(0)==False and lcd.pressed(1)==False and lcd.pressed(2)==False and lcd.pressed(3)==False:
			lcd.setcurpos(0,1)
			lcd.putstring("             ")

	except:
		continue


