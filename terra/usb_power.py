import time
import ablib
 
Power_USB_A = ablib.Pin('N','7','high')
Power_USB_B = ablib.Pin('N','8','high')
Power_USB_C = ablib.Pin('N','9','high')

while True:
	print "USB A OFF"
	Power_USB_A.off()
	time.sleep(1) 

	print "USB B OFF"
	Power_USB_B.off()
	time.sleep(1) 

	print "USB C OFF"
	Power_USB_C.off()
	time.sleep(1) 

	print "USB A ON"
	Power_USB_A.on()
	time.sleep(1) 

	print "USB B ON"
	Power_USB_B.on()
	time.sleep(1) 

	print "USB C ON"
	Power_USB_C.on()
	time.sleep(1) 

