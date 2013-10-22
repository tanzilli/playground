import ablib
import time

lcd = ablib.Daisy24(0)
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




