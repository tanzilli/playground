import ablib
import time

lcd = ablib.Daisy24()

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

