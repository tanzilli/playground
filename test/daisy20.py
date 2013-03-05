#Factory test for Daisy-20 boards

import ablib
import time

#0x27 for PCF8474 T
#0x3F for PCF8474 AT
 
LCD_ADDRESS = 0x27

lcd = ablib.Daisy24(0,LCD_ADDRESS)

lcd.backlighton()
lcd.putstring("Test Daisy-20)

while True:
	if lcd.pressed(0):
		print "Key 0 pressed"
		lcd.home()
		lcd.putstring("Backlight ON ")
		lcd.backlighton()
	else:
		lcd.home()
		lcd.putstring("Backlight OFF")
		lcd.backlightoff()

	if lcd.pressed(0):
		lcd.setcurpos(0,1)
		lcd.putstring("Key 0 pressed")

	if lcd.pressed(1):
		lcd.setcurpos(0,1)
		lcd.putstring("Key 1 pressed")

	if lcd.pressed(2):
		lcd.setcurpos(0,1)
		lcd.putstring("Key 2 pressed")

	if lcd.pressed(3):
		lcd.setcurpos(0,1)
		lcd.putstring("Key 3 pressed")


	if  lcd.pressed(0)==False and lcd.pressed(1)==False and lcd.pressed(2)==False and lcd.pressed(3)==False:
		lcd.setcurpos(0,1)
		lcd.putstring("             ")

	time.sleep(0.2)

