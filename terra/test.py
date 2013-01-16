import ablib
import time
import serial
import sys
import select

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

	while True:
		print ""
		print "Modem tests"
		print "----------------------"
		print "1 - Modem power section ON" 
		print "2 - Modem power section OFF" 
		print "3 - Send a pulse on modem power_key" 
		print "4 - Send a SMS"
		print "q - Quit"
		print "----------------------"

		print "Select:",
		test_to_run=getch()
		if test_to_run=="q":
			return
		print " "

		if test_to_run=="1":
			print "Modem power section ON"
			quectel_power.on()

		if test_to_run=="2":
			print "Modem power section OFF"
			quectel_power.off()

		if test_to_run=="3":
			print "Send a pulse on modem power_key"
			quectel_power_key.on()
			time.sleep(1)
			quectel_power_key.off()

		if test_to_run=="4":
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


def usb_tests():
	while True:
		print ""
		print "USB tests"
		print "----------------------"
		print "a - Toggle USB A power"
		print "b - Toggle USB B power"
		print "c - Toggle USB C power"
		print "q - Quit"
		print "----------------------"

		print "Select:",
		test_to_run=getch()
		if test_to_run=="q":
			return
		print " "

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

def slide(kid_dictionary):
	for key in sorted(kid_dictionary.iterkeys()):
		if kid_dictionary[key]!=0:
			print "%s: %s" % (key,kid_dictionary[key])
			ablib.export(kid_dictionary[key])
			ablib.direction(kid_dictionary[key],"out")
			ablib.set_value(kid_dictionary[key],0)

	for key in sorted(kid_dictionary.iterkeys()):
		if kid_dictionary[key]!=0:
			ablib.set_value(kid_dictionary[key],1)
			time.sleep(0.2)

	for key in sorted(kid_dictionary.iterkeys()):
		if kid_dictionary[key]!=0:
			ablib.set_value(kid_dictionary[key],0)
			time.sleep(0.2)



def d_tests():
	while True:
		print ""
		print "Daisy connector tests"
		print "----------------------"
		print "0 - D10"
		print "1 - D11"
		print "2 - D12"
		print "3 - D13"
		print "4 - D14"
		print "5 - D15"
		print "6 - D16"
		print "q - Quit"
		print "----------------------"

		print "Select:",
		test_to_run=getch()
		if test_to_run=="q":
			return
		print " "

		connector="D1"+test_to_run;

		if connector=="D10":
			print "Connector D10"
			kid_dictionary=ablib.D10_kernel_ids
			slide(kid_dictionary)

		if connector=="D11":
			print "Connector D11"
			kid_dictionary=ablib.D11_kernel_ids
			slide(kid_dictionary)

		if connector=="D12":
			print "Connector D12"
			kid_dictionary=ablib.D12_kernel_ids
			slide(kid_dictionary)

		if connector=="D13":
			print "Connector D13"
			kid_dictionary=ablib.D13_kernel_ids
			slide(kid_dictionary)

		if connector=="D14":
			print "Connector D14"
			kid_dictionary=ablib.D14_kernel_ids
			slide(kid_dictionary)

		if connector=="D15":
			print "Connector D15"
			kid_dictionary=ablib.D15_kernel_ids
			slide(kid_dictionary)

		if connector=="D16":
			print "Connector D16"
			kid_dictionary=ablib.D16_kernel_ids
			slide(kid_dictionary)

quectel_power = ablib.Pin('W','10','low')
quectel_power_key = ablib.Pin('E','10','low')

usb_a_power = ablib.Pin('N','7','high')
usb_b_power = ablib.Pin('N','8','high')
usb_c_power = ablib.Pin('N','9','high')

getch=_GetchUnix()
while True:

	print ""
	print "Terra tests"
	print "----------------------"
	print "m - Modem tests" 
	print "u - USB tests" 
	print "d - Daisy connector tests" 
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

	if test_to_run=="u":
		usb_tests()

	if test_to_run=="d":
		d_tests()

