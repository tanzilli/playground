import ablib
import time

lcd = ablib.Daisy24()
lcd.backlighton()

while True:
	for x in range(0,16,12):
		for y in range(2):
			for counter in range (1000+1):
				lcd.setcurpos(x,y)
				lcd.putstring("%4s" % counter)





