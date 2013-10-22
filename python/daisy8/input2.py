from ablib import Daisy8
from time import sleep

IN0_A = Daisy8('D11','IN0','first')
IN1_A = Daisy8('D11','IN1','first')
IN0_B = Daisy8('D11','IN0','second')
IN1_B = Daisy8('D11','IN1','second')
 
while True:
	print " IN0 first=", IN0_A.get()
	print " IN1 first=", IN1_A.get()
	print "IN0 second=", IN0_B.get()
	print "IN1 second=", IN1_B.get()
	sleep(1)
