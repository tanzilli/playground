import ablib
import time

#Daisy-24 I/O expander chip address. Use:
#0x27 for PCF8474 T
#0x3F for PCF8474 AT
 
LCD_ADDRESS = 0x27


while True:
	try:
		lcd = ablib.Daisy24(0,LCD_ADDRESS)
		lcd.putstring("Test Daisy-24")
	except:
		continue

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

	time.sleep(0.2)

