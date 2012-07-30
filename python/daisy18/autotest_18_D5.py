import ablib
import time

# Tests the first bits in input for Daisy18
# Daisy18 module wired on D2 connector


Mon1 = ablib.Daisy11('D2','L1')
Mon2 = ablib.Daisy11('D2','L2')
Mon3 = ablib.Daisy11('D2','L3')
Mon4 = ablib.Daisy11('D2','L4')

Act18 = ablib.Daisy11('D2','L8')
Act19 = ablib.Daisy11('D2','L7')

MonOk = ablib.Daisy11('D2','L6')
MonErr = ablib.Daisy11('D2','L5')


SlowTest = ablib.Daisy5('D3','P5')
SelD18 = ablib.Daisy5('D3','P7')
SelD19 = ablib.Daisy5('D3','P8')

testD18=False
testD19=False
selTest= True
blinkOn=True
testDelay=0.1

print "Select Test : "

while selTest:
	
	if blinkOn:
		Mon1.on()
		Mon2.off()
		Mon3.on()
		Mon4.off()
		blinkOn=False
	else:
		Mon2.on()
		Mon1.off()
		Mon4.on()
		Mon3.off()
		blinkOn=True
	time.sleep(testDelay)
	
	if SelD18.pressed():
		testD18=True
		selTest=False
		In1 = ablib.Daisy18('D5','first','I1')
		In2 = ablib.Daisy18('D5','first','I2')
		In3 = ablib.Daisy18('D5','first','I3')
		In4 = ablib.Daisy18('D5','first','I4')
		 
		Out1 = ablib.Daisy19('D5','second','O1')
		Out2 = ablib.Daisy19('D5','second','O2')
		Out3 = ablib.Daisy19('D5','second','O3')
		Out4 = ablib.Daisy19('D5','second','O4')
		Act18.on()
		print "Start Test D18"

	if SelD19.pressed():
		testD19=True
		selTest=False
		In1 = ablib.Daisy18('D5','second','I1')
		In2 = ablib.Daisy18('D5','second','I2')
		In3 = ablib.Daisy18('D5','second','I3')
		In4 = ablib.Daisy18('D5','second','I4')
		 
		Out1 = ablib.Daisy19('D5','first','O1')
		Out2 = ablib.Daisy19('D5','first','O2')
		Out3 = ablib.Daisy19('D5','first','O3')
		Out4 = ablib.Daisy19('D5','first','O4')
		Act19.on()
		print "Start Test D19"
		

 
while True:
	blnTestOk=True
	Out1.on()
	time.sleep(testDelay)
	if In1.activated():
		print "In 1 H OK  ",
		Mon1.on()
	else:
		print "In 1 H ERR ",
		blnTestOk=False
		Mon1.off()
	Out1.off()
	time.sleep(testDelay)
	if not In1.activated():
		print "L OK  ",
		Mon1.off()
	else:
		print "L ERR ",
		Mon1.on()
		blnTestOk=False

		
	Out2.on()
	time.sleep(testDelay)
	if In2.activated():
		print "In 2 H OK ",
		Mon2.on()
	else:
		print "In 2 H ERR",
		Mon2.off()
		blnTestOk=False
	Out2.off()
	time.sleep(testDelay)
	if not In2.activated():
		print "L OK ",
		Mon2.off()
	else:
		print "L ERR",
		Mon2.on()
		blnTestOk=False
	
	Out3.on()
	time.sleep(testDelay)
	if In3.activated():
		print "In 3 H OK ",
		Mon3.on()
	else:
		print "In 3 H ERR",
		Mon3.off()
		blnTestOk=False
	Out3.off()
	time.sleep(testDelay)
	if not In3.activated():
		print "L OK ",
		Mon3.off()
	else:
		print "L ERR",
		Mon3.on()
		blnTestOk=False
	
	Out4.on()
	time.sleep(testDelay)		
	if In4.activated():
		print "In 4 H OK ",
		Mon4.on()
	else:
		print "In 4 H ERR",
		Mon4.off()
		blnTestOk=False
	Out4.off()
	time.sleep(testDelay)
	if not In4.activated():
		print "L OK "
		Mon4.off()
	else:
		print "L ERR"
		Mon4.on()
		blnTestOk=False

	if blnTestOk:
		MonOk.on()
		MonErr.off()
	else:
		MonOk.off()
		if blinkOn:
			MonErr.on()
			blinkOn=False
		else:
			MonErr.off()
			blinkOn=True

	if SlowTest.pressed():
		testDelay=0.3
	else:
		testDelay=0.1
