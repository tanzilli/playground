import ablib
import time

lcd = ablib.Daisy14(0,0x20)
lcd.setcurpos(0,0)
lcd.putstring("Line 0")
lcd.setcurpos(0,1)
lcd.putstring("Line 1")
lcd.setcurpos(0,2)
lcd.putstring("Line 2")
lcd.setcurpos(0,3)
lcd.putstring("Line 3")
