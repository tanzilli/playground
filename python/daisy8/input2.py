import ablib
import time

IN0_A = ablib.Daisy8(connector='D11',id='IN0',position='first')
IN1_A = ablib.Daisy8(connector='D11',id='IN1',position='first')
IN0_B = ablib.Daisy8(connector='D11',id='IN0',position='second')
IN1_B = ablib.Daisy8(connector='D11',id='IN1',position='second')
 
while True:
	print " IN0 first=", IN0_A.get()
	print " IN1 first=", IN1_A.get()
	print "IN0 second=", IN0_B.get()
	print "IN1 second=", IN1_B.get()

	time.sleep(1)
