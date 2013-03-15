import ablib
import time

#Use D2 or D5 on the FOX Board G20
#Use D11 or D12 on the Terra board

connector="D11"

In1 = ablib.Daisy18(connector,'first','CH1')
In2 = ablib.Daisy18(connector,'first','CH2')
In3 = ablib.Daisy18(connector,'first','CH3')
In4 = ablib.Daisy18(connector,'first','CH4')
 
print "Start reading..."
print "Press ctrl-c to exit"
 
while True:
	if In1.state():
		print "CH1 active"
		time.sleep(0.5)
	if In2.state():
		print "CH2 active"
		time.sleep(0.5)
	if In3.state():
		print "CH3 active"
		time.sleep(0.5)
	if In4.state():
		print "CH4 active"
		time.sleep(0.5)
