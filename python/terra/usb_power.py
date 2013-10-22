from time import sleep
from ablib import Pin
 
Power_USB_A = Pin('N7','HIGH')
Power_USB_B = Pin('N8','HIGH')
Power_USB_C = Pin('N9','HIGH')

while True:
	print "USB A OFF"
	Power_USB_A.off()
	sleep(1) 

	print "USB B OFF"
	Power_USB_B.off()
	sleep(1) 

	print "USB C OFF"
	Power_USB_C.off()
	sleep(1) 

	print "USB A ON"
	Power_USB_A.on()
	sleep(1) 

	print "USB B ON"
	Power_USB_B.on()
	sleep(1) 

	print "USB C ON"
	Power_USB_C.on()
	sleep(1) 

