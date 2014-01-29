from ablib import Daisy8
from time import sleep

IN0 = Daisy8('D11','first','IN0')
IN1 = Daisy8('D11','first','IN1')
 
while True:
	print "IN0=", IN0.get()
	sleep(1)
	print "IN1=", IN1.get()
	sleep(1)


