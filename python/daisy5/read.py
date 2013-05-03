import ablib

connector="D11"

# Create an istance for each button

P1 = ablib.Daisy5(connector,'P1')
P2 = ablib.Daisy5(connector,'P2')
P3 = ablib.Daisy5(connector,'P3')
P4 = ablib.Daisy5(connector,'P4')
P5 = ablib.Daisy5(connector,'P5')
P6 = ablib.Daisy5(connector,'P6')
P7 = ablib.Daisy5(connector,'P7')
P8 = ablib.Daisy5(connector,'P8')

# Poll on each butto to check if pressed
while True:
	if (P1.get()):
		print "P1 pressed" 
	if (P2.get()):
		print "P2 pressed" 
	if (P3.get()):
		print "P3 pressed" 
	if (P4.get()):
		print "P4 pressed" 
	if (P5.get()):
		print "P5 pressed" 
	if (P6.get()):
		print "P6 pressed" 
	if (P7.get()):
		print "P7 pressed" 
	if (P8.get()):
		print "P8 pressed" 


