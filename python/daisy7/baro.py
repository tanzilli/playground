from time import sleep
from ablib import Daisy7

memsgps = Daisy7("D10")
while True:
	print "Temperature: %.2f C" % memsgps.baro_getTemperature()
	print "   Pressure: %.2f hPa" % (memsgps.baro_getPressure()/100.0)
	print "   Altitude: %.2f" % memsgps.baro_getAltitude()
	print ""

	sleep(0.5)
