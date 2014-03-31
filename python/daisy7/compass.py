from time import sleep
from ablib import Daisy7

memsgps = Daisy7("D10")
while True:
	(x,y,z)= memsgps.compass_getAxes()
	print "X=%6d Y=%6d Z=%6d" % (x,y,z)
	sleep(0.5)
	
