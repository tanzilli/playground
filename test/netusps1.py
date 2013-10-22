import ablib
import time

OUT_3V3=0
OUT_3V25=1
OUT_1V8=2
OUT_1V0=3

Shutdown=ablib.Daisy8(connector='D2',id='RL1')
VIN_5V=ablib.Daisy8(connector='D2',id='RL0')

def adc(ch):
	VREF=5.12
	volt_per_point=VREF/(2**10)
	path="/sys/bus/platform/devices/at91_adc/"

	fd = open(path + "chan" + str(ch),"r")
	sample = fd.read()
	fd.close()
	return int(sample)*volt_per_point

def leggi():
	while True:
		a=adc(OUT_3V3)
		print "%.1f %.1f %.1f %.1f " % (adc(OUT_3V3),adc(OUT_3V25),adc(OUT_1V8),adc(OUT_1V0))
	
def getinput():
	rtc= "%.1f %.1f %.1f %.1f " % (adc(OUT_3V3),adc(OUT_3V25),adc(OUT_1V8),adc(OUT_1V0))
	return rtc

def message(linea1="",linea2="",timeout=-1):
	lcd.clear()
	lcd.putstring("%-16s" % linea1)
	lcd.setcurpos(0,1)
	lcd.putstring("%-16s" % linea2)

	if timeout>-1:
		timeout=400*timeout	

	while (lcd.pressed(0) or lcd.pressed(1) or lcd.pressed(2) or lcd.pressed(3))==False:
		if timeout>-1:
			timeout=timeout-1	
			if timeout==0:
				return	

	while(lcd.pressed(0) or lcd.pressed(1) or lcd.pressed(2) or lcd.pressed(3))==True:	
		pass


lcd = ablib.Daisy24(0)
lcd.backlighton()

lcd.putstring("Test NETUSPS1")
time.sleep(1)

VIN_5V.off()
Shutdown.off()

POK = ablib.Daisy8(connector='D2',id='IN0')

counter_ok=0
message_timeout=4
while True:
	VIN_5V.off()
	Shutdown.off()

	message("Netus PS1","Press to run--->")
	lcd.clear()
	lcd.putstring("Wait...")

	#Accendo i 5 volt e controllo che le tensioni siano corrette
	VIN_5V.on()
	time.sleep(1)

	a=adc(OUT_3V3) #La prima lettura a vuoto serve
	line_3V3=adc(OUT_3V3)
	line_3V25=adc(OUT_3V25)
	line_1V8=adc(OUT_1V8)
	line_1V0=adc(OUT_1V0)
	
	bad=False
	if line_3V3<3.0 or line_3V3>3.5:
		bad=True
	if line_3V25<3.0 or line_3V25>3.4:
		bad=True
	if line_1V8<1.7 or line_1V8>1.9:
		bad=True
	if line_1V0<0.0 or line_1V0>1.1:
		bad=True
	
	if bad:	
		message("Errore:","%.1f %.1f %.1f %.1f " % (line_3V3,line_3V25,line_1V8,line_1V0),message_timeout)
		continue
	
	message("Accensione: OK  ",getinput(),message_timeout-2)
	lcd.clear()
	lcd.putstring("Wait...")
	Shutdown.on()
	time.sleep(1)

	a=adc(OUT_3V3) #La prima lettura a vuoto serve
	line_3V3=adc(OUT_3V3)
	line_3V25=adc(OUT_3V25)
	line_1V8=adc(OUT_1V8)
	line_1V0=adc(OUT_1V0)
	
	bad=False
	if line_3V3>0.1:
		bad=True
	if line_3V25<3.0 or line_3V25>3.4:
		bad=True
	if line_1V8>0.1:
		bad=True
	if line_1V0>0.1:
		bad=True
	
	if bad:	
		message("Errore:","%.1f %.1f %.1f %.1f " % (line_3V3,line_3V25,line_1V8,line_1V0),message_timeout)
		continue

	message("Shutdown: OK:","%.1f %.1f %.1f %.1f " % (line_3V3,line_3V25,line_1V8,line_1V0),message_timeout)
