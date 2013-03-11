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
	print "Wait..."
	time.sleep(5)
	print "Send [%s] SMS to [%s]" % (message,send_to)
	ser.write("AT+CMGF=1\r")
	print ser.readlines()
	ser.write("AT+CMGS=" + "\"" + send_to + "\"" + "\r")
	time.sleep(0.5);
	ser.write(message + "\x1a")
	time.sleep(1);
	print ser.readlines()
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


def modem_terminal(serial,string,timeout):
	serial.flushInput()
	serial.write(string)
	while timeout>0:
		if serial.inWaiting()>0:
			sys.stdout.write(serial.read(serial.inWaiting()))
		time.sleep(0.001)
		timeout=timeout-1
	print ""


quectel_power = ablib.Pin('W','10','high')
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

ttyS1 = serial.Serial(
	port='/dev/ttyS1', 
	baudrate=9600, 
	timeout=0.5,
	parity=serial.PARITY_NONE,
	stopbits=serial.STOPBITS_ONE,
	bytesize=serial.EIGHTBITS
)  


getch=_GetchUnix()
while True:

	print ""
	print "Terra tests"
	print "----------------------"
	print "1 - Modem ON" 
	print "2 - Check serial link (Send AT on /dev/ttyS1)" 
	print "4 - Modem OFF" 
	print "s - Send a SMS" 
	print "a - Toggle USB A power" 
	print "b - Toggle USB A power" 
	print "c - Toggle USB A power" 
	print "q - Quit"
	print "----------------------"

	print "Select: ",
	test_to_run=getch()
	if test_to_run=="q":
		ttyS1.close()
		print "Goodbye cruel world !"
		quit()
	print " "

	#Modem ON
	if test_to_run=="1":
		print "Modem power section ON"
		quectel_power.on()
		time.sleep(1)
		print "Send a power key pulse to the modem"
		quectel_power_key.on()
		time.sleep(1)
		quectel_power_key.off()

	#Test serial link
	if test_to_run=="2":
		modem_terminal(ttyS1,"AT\r",200)

	#Make a call to myself
	#if test_to_run=="3":
	#	modem_terminal(ttyS1,"ATDT404\r",10000)

	#Send a SMS
	if test_to_run=="s":
		send_to = "+393460624344"
		message = "Hello world !"
		print "Wait..."
		time.sleep(5)
		print "Send [%s] SMS to [%s]" % (message,send_to)
		ttyS1.write("AT+CMGF=1\r")
		print ttyS1.readlines()
		ttyS1.write("AT+CMGS=" + "\"" + send_to + "\"" + "\r")
		time.sleep(0.5);
		ttyS1.write(message + "\x1a")
		time.sleep(1);
		print ttyS1.readlines()

	#Modem OFF
	if test_to_run=="4":
		quectel_power.off()

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

