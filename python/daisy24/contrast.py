import ablib
import time

#Check for Daisy-24 address
if ablib.existI2Cdevice(0,0x27):
	i2c_address=0x27
else:
	i2c_address=0x3F

lcd = ablib.Daisy24(0,i2c_address)
lcd.backlighton()

lcd.putstring("Hello World !")

while True:
	i=0
	while i<10:
		i+=1
		lcd.setcontrast(i)
		time.sleep(0.1)

	while i>0:
		i-=1
		lcd.setcontrast(i)
		time.sleep(0.1)




