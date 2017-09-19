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
	lcd.clear()
	lcd.setdoublefont()
	lcd.putstring("Hello World !")

	time.sleep(1)

	lcd.clear()
	lcd.setsinglefont()
	lcd.putstring("Hello World !")

	time.sleep(1)

