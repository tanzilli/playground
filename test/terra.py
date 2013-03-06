#Factory Terra board benchtest

#Power control on USB ports
#D10 to D16 daisy connectors
#GPRS Modem

#To use this program it is requested to have a full gpio Kernel image

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

def modem_tests():
	# Insert here the destination number
	send_to = "+393460624344"
	message = "Hello world !"

	print "Modem power section ON"
	quectel_power.off()
	time.sleep(1)
	quectel_power.on()
	time.sleep(1)
	print "Send a pulse on modem power_key"
	quectel_power_key.on()
	time.sleep(1)
	quectel_power_key.off()
	print "Wait..."
	time.sleep(5)
	print "Send [%s] SMS to [%s]" % (message,send_to)
	ser = serial.Serial(
		port='/dev/ttyS1', 
		baudrate=115200, 
		timeout=5,
		parity=serial.PARITY_NONE,
		stopbits=serial.STOPBITS_ONE,
		bytesize=serial.EIGHTBITS
	)  
	ser.write("AT\r")
	print ser.readlines()
	ser.write("AT\r")
	print ser.readlines()
	ser.write("AT\r")
	print ser.readlines()
	ser.write("AT+CMGF=1\r")
	print ser.readlines()
	ser.write("AT+CMGS=" + "\"" + send_to + "\"" + "\r")
	time.sleep(0.5);
	ser.write(message + "\x1a")
	time.sleep(1);
	print ser.readlines()
	ser.close()
	return

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


quectel_power = ablib.Pin('W','10','low')
quectel_power_key = ablib.Pin('E','10','low')

usb_a_power = ablib.Pin('N','7','high')
usb_b_power = ablib.Pin('N','8','high')
usb_c_power = ablib.Pin('N','9','high')

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

getch=_GetchUnix()
while True:

	print ""
	print "Terra tests"
	print "----------------------"
	print "m - Modem tests" 
	print "a - Toggle USB A power" 
	print "b - Toggle USB A power" 
	print "c - Toggle USB A power" 
	print "q - Quit"
	print "----------------------"

	print "Select: ",
	test_to_run=getch()
	if test_to_run=="q":
		print "Goodbye cruel world !"
		quit()
	print " "

	if test_to_run=="m":
		modem_tests()

	if test_to_run=="a":
		if usb_a_power.get_value()==0:
			print "USB A on"
			usb_a_power.on()
		else:
			print "USB A off"
			usb_a_power.off()

	if test_to_run=="b":
		if usb_b_power.get_value()==0:
			print "USB B on"
			usb_b_power.on()
		else:
			print "USB B off"
			usb_b_power.off()

	if test_to_run=="c":
		if usb_c_power.get_value()==0:
			print "USB C on"
			usb_c_power.on()
		else:
			print "USB C off"
			usb_c_power.off()

