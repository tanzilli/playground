import ablib
import time

Out_1V0=0
Out_1V8=1
Out_3V25=2
Out_3V3=3

Shutdown=ablib.Daisy8(connector='D2',id='RL1')
Alimentazione=ablib.Daisy8(connector='D2',id='RL0')

def adc(ch):
	VREF=10.0
	volt_per_point=VREF/(2**10)
	path="/sys/bus/platform/devices/at91_adc/"

	fd = open(path + "chan" + str(ch),"r")
	sample = fd.read()
	fd.close()
	return int(sample)*volt_per_point

def leggi():
	print "    Out_1V0  %.2f" % adc(Out_1V0)
	print "    Out_1V8  %.2f" % adc(Out_1V8)
	print "    Out_3V25 %.2f" % adc(Out_3V25)
	print "    Out_3V3  %.2f" % adc(Out_3V3)


lcd = ablib.Daisy24(0)
lcd.backlighton()

lcd.putstring("Test NETUSPS1")

Alimentazione.off()
Shutdown.off()

POK = ablib.Daisy8(connector='D2',id='IN0')

while True:
	while True:
		lcd.clear()
		lcd.putstring("Press---------->")
		while lcd.pressed(0)==False:
			time.sleep(0.1)	
		break	

	print 
	print("**************")
	print("* START    ***")
	print("**************")

	Alimentazione.off()
	Shutdown.off()
	print("OFF")
	for i in range (3):
		print("  Wait 0.5 sec")
		print "  Lettura: ",i
		time.sleep(0.5)
		leggi()

	Alimentazione.on()
	Shutdown.off()
	print("ON")
	for i in range (3):
		print("  Wait 0.5 sec")
		print "  Lettura: ",i
		time.sleep(0.5)
		leggi()

	Alimentazione.on()
	Shutdown.on()
	print("ON")
	print("SHUTDOWN")
	for i in range (3):
		print("  Wait 0.5 sec")
		print "  Lettura: ",i
		time.sleep(0.5)
		leggi()

	Alimentazione.on()
	Shutdown.off()
	print("ON")
	for i in range (3):
		print("  Wait 0.5 sec")
		print "  Lettura: ",i
		time.sleep(0.5)
		leggi()

	print("OFF")
	Alimentazione.off()
	Shutdown.off()
	for i in range (3):
		print("  Wait 0.5 sec")
		print "  Lettura: ",i
		time.sleep(0.5)
		leggi()

