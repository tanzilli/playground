import ablib
import time

lcd = ablib.Daisy24(0)
lcd.backlighton()
lcd.putstring("Hello World !")

