import ablib
import time

IN0 = ablib.Daisy8(connector='D11',id='IN0')
IN1 = ablib.Daisy8(connector='D11',id='IN1')
 
while True:
	print "IN0=", IN0.get()
	time.sleep(1)
	print "IN1=", IN1.get()
	time.sleep(1)


