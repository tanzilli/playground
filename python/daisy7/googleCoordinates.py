from ablib import Daisy7

memsgps = Daisy7("D10")
while True:
	(latitude,longitude)=memsgps.gps_getGoogleCoordinates()
	if latitude==-1:
			continue
	print "     Latitude: ",latitude
	print "    Longitude: ",longitude
	print "          URL: https://maps.google.com/maps?q=%f,%f" % (latitude,longitude)
	print ""
