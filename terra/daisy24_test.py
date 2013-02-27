#Daisy-24 benchtest using a Terra board

import ablib
import time
import sys
import select

#Daisy-24 I/O expander chip address. Use:
#0x27 for PCF8474 T
#0x3F for PCF8474 AT

def lcd_test(lcd_address):
 
	lcd = ablib.Daisy24(0,lcd_address)

	a=0;
	lcd.backlightoff()
	while a<>0x0F:
		if lcd.pressed(0):
			lcd.setcurpos(0,1)
			lcd.putstring("Key 0 pressed")
			lcd.backlighton()
			time.sleep(0.5)
			lcd.backlightoff()

		if lcd.pressed(1):
			lcd.setcurpos(0,1)
			lcd.putstring("Key 1 pressed")
			lcd.backlighton()
			time.sleep(0.5)
			lcd.backlightoff()

		if lcd.pressed(2):
			lcd.setcurpos(0,1)
			lcd.putstring("Key 2 pressed")
			lcd.backlighton()
			time.sleep(0.5)
			lcd.backlightoff()

		if lcd.pressed(3):
			lcd.setcurpos(0,1)
			lcd.putstring("Key 3 pressed")
			lcd.backlighton()
			time.sleep(0.5)
			lcd.backlightoff()

		if  lcd.pressed(0)==False and lcd.pressed(1)==False and lcd.pressed(2)==False and lcd.pressed(3)==False:
			lcd.setcurpos(0,1)
			lcd.putstring("             ")

		time.sleep(0.2)

class _GetchUnix:
  def __init__(self):
		import tty, sys
	def __call__(self):
		import sys, tty, termios
		fd = sys.stdin.fileno()
		old_settings = termios.tcgetattr(fd)
		try:
			tty.setraw(sys.stdin.fileno())
			ch = sys.stdin.read(1)
		finally:
			termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
		return ch


getch=_GetchUnix()

while True:

	print ""
	print "Terra tests"
	print "----------------------"
	print "1 - Daisy-24 with PCF8474 T" 
	print "2 - Daisy-24 with PCF8474 AT" 
	print "q - Quit"
	print "----------------------"

	print "Select: ",
	test_to_run=getch()
	if test_to_run=="q":
		print "Goodbye cruel world !"
		quit()
	if test_to_run=="1":
		try:
			lcd_test(0x27)
	if test_to_run=="2":
		try:
			lcd_test(0x3E)
	print " "



