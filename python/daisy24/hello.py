import ablib
import time

lcd = ablib.Daisy24()
lcd.backlighton()
lcd.putstring("Hello World !")

