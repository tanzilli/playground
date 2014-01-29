from ablib import Daisy8
from time import sleep

IN0_A = Daisy8('D11','first','IN0')
IN1_A = Daisy8('D11','first','IN1')
IN0_B = Daisy8('D11','second','IN0')
IN1_B = Daisy8('D11','second','IN1')
 
while True:
	print " IN0 first=", IN0_A.get()
	print " IN1 first=", IN1_A.get()
	print "IN0 second=", IN0_B.get()
	print "IN1 second=", IN1_B.get()
	sleep(1)
