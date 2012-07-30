#!/usr/bin/python

#Read the voltage values from the 
#built-in ADC
#http://www.acmesystems.it/foxg20_adc
 
import time 

VREF=3.24
volt_per_point=VREF/2**10
path="/sys/bus/platform/devices/at91_adc/"

ch=0
while True:

	fd = open(path + "chan" + str(ch),"r")
	sample = fd.read()
	print "Channel %d = %.2f volt" % (ch,int(sample)*volt_per_point)
	fd.close()
	time.sleep(0.5)
	ch+=1
	if ch==4: 
		ch=0
		print "-------"


