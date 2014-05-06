#Factory test for AriaG25-ek

#D10 to D17 daisy connectors 

import ablib
import time
import serial
import sys
import select
import thread
import threading

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

def slide(kid_dictionary,a):
	while True:
		for key in sorted(kid_dictionary.iterkeys()):
			if kid_dictionary[key]!=0:
				ablib.export(kid_dictionary[key])
				ablib.direction(kid_dictionary[key],"out")
				ablib.set_value(kid_dictionary[key],0)

		for key in sorted(kid_dictionary.iterkeys()):
			if kid_dictionary[key]!=0:
				ablib.set_value(kid_dictionary[key],1)
				time.sleep(0.1)
				ablib.set_value(kid_dictionary[key],0)
				time.sleep(0.01)

def modem_terminal(serial,string,timeout):
	serial.flushInput()
	serial.write(string)
	while timeout>0:
		if serial.inWaiting()>0:
			sys.stdout.write(serial.read(serial.inWaiting()))
		time.sleep(0.001)
		timeout=timeout-1
	print ""

kid_dictionary=ablib.D10_kernel_ids
thread.start_new_thread(slide,(kid_dictionary,1))
kid_dictionary=ablib.D11_kernel_ids
thread.start_new_thread(slide,(kid_dictionary,1))
kid_dictionary=ablib.D12_kernel_ids
thread.start_new_thread(slide,(kid_dictionary,1))
kid_dictionary=ablib.D13_kernel_ids
thread.start_new_thread(slide,(kid_dictionary,1))
kid_dictionary=ablib.D14_kernel_ids
thread.start_new_thread(slide,(kid_dictionary,1))
kid_dictionary=ablib.D15_kernel_ids
thread.start_new_thread(slide,(kid_dictionary,1))
kid_dictionary=ablib.D16_kernel_ids
thread.start_new_thread(slide,(kid_dictionary,1))
kid_dictionary=ablib.D17_kernel_ids
thread.start_new_thread(slide,(kid_dictionary,1))

getch=_GetchUnix()
while True:

	print ""
	print "AriaG25-ek tests"
	print "----------------------"
	print "q - Quit"
	print "----------------------"

	print "Select: ",
	test_to_run=getch()
	if test_to_run=="q":
		ttyS1.close()
		print "Goodbye cruel world !"
		quit()
	print " "

