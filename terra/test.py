import ablib
import time
import serial
 
def menu():
	print ""
	print "Test ARIAG25-EB"
	print "----------------------"
	print "1 - Quectel ON" 
	print "2 - Quectel OFF" 
	print "3 - Pulse on power key" 
	print "4 - Send a SMS"

	print "a - USB A on/off" 
	print "b - USB B on/off" 
	print "c - USB B on/off" 

	print "x - Esci" 
	print "----------------------"
 
 
quectel_power = ablib.Pin('W','10','low')
quectel_power_key = ablib.Pin('E','10','low')

usb_a_power = ablib.Pin('N','7','low')
usb_b_power = ablib.Pin('N','8','low')
usb_c_power = ablib.Pin('N','9','low')

# Insert here the destination number
send_to = "+393460624344"
message = "Hello world !"

while True:
	menu()
	scelta=raw_input("Scegli:")
	print " "

	if scelta=="a":
		if usb_a_power.get_value()==0:
			print "USB A on"
			usb_a_power.on()
		else:
			print "USB A off"
			usb_a_power.off()

	if scelta=="b":
		if usb_b_power.get_value()==0:
			print "USB B on"
			usb_b_power.on()
		else:
			print "USB B off"
			usb_b_power.off()

	if scelta=="c":
		if usb_c_power.get_value()==0:
			print "USB C on"
			usb_c_power.on()
		else:
			print "USB C off"
			usb_c_power.off()

	if scelta=="1":
		print "Accendo il Quectel"
		quectel_power.on()

	if scelta=="2":
		print "Spengo il Quectel"
		quectel_power.off()

	if scelta=="3":
		print "Pulse on power key"
		quectel_power_key.on()
		time.sleep(1)
		quectel_power_key.off()
		print "End of pulse"

	if scelta=="4":
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
		
	if scelta=="x":
		print "Addio mondo crudele !"
		quit()



