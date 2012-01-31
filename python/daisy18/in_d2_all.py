import fox
import time

# Tests the first bits in input for Daisy18
# Daisy18 module wired on D2 connector

In1 = fox.Daisy18('D2','first','I1')
In2 = fox.Daisy18('D2','first','I2')
In3 = fox.Daisy18('D2','first','I3')
In4 = fox.Daisy18('D2','first','I4')
In5 = fox.Daisy18('D2','second','I1')
In6 = fox.Daisy18('D2','second','I2')
In7 = fox.Daisy18('D2','second','I3')
In8 = fox.Daisy18('D2','second','I4')

print "Start Test"
 
while True:
	if In1.activated():
		print "In 1 On  ",
	else:
		print "In 1 Off ",
		
	if In2.activated():
		print "In 2 On  ",
	else:
		print "In 2 Off ",
		
	if In3.activated():
		print "In 3 On  ",
	else:
		print "In 3 Off ",

	if In4.activated():
		print "In 4 On  ",
	else:
		print "In 4 Off ",

	if In5.activated():
		print "In 5 On  ",
	else:
		print "In 5 Off ",

	if In6.activated():
		print "In 6 On  ",
	else:
		print "In 6 Off ",
		
	if In7.activated():
		print "In 7 On  ",
	else:
		print "In 7 Off ",		

	if In8.activated():
		print "In 8 On  ",
	else:
		print "In 8 Off ",		
	
	print ""
	time.sleep(0.5)
