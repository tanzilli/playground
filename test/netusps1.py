import ablib
import time

OUT_3V3=0
OUT_3V25=1
OUT_1V8=2
OUT_1V0=3

Shutdown=ablib.Daisy8(connector='D2',id='RL1')
VIN_5V=ablib.Daisy8(connector='D2',id='RL0')

def adc(ch):
	VREF=3.25
	volt_per_point=VREF/(2**10)
	path="/sys/bus/platform/devices/at91_adc/"

	fd = open(path + "chan" + str(ch),"r")
	sample = fd.read()
	fd.close()
	return int(sample)*volt_per_point

def leggi():
	print "%.2f %.2f %.2f %.2f " % (adc(OUT_3V3),adc(OUT_3V25),adc(OUT_1V8),adc(OUT_1V0))

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

	message("Power OFF","Hit to start    ")

	#Controllo che tutte le tensioni siano a zero	
	a=adc(OUT_3V25)
	total_out = adc(OUT_3V3)+adc(OUT_3V25)+adc(OUT_1V8)+adc(OUT_1V0)
	if total_out>0.2:
		message("Errore:","OUT non 0V")
		continue

	#Accendo la VIN a 5 volt e controllo subito la 3V25
	VIN_5V.on()
	time.sleep(0.2)
	a=adc(OUT_3V25)
	a=adc(OUT_3V25)
	if a<3.00:
		message("Errore:","NO 3V25 %.2fv" % adc(OUT_3V25),message_timeout)
		a=adc(OUT_3V25)
		continue

	vcount=0
	while adc(OUT_1V0)<1:
		vcount=vcount+1;
		if vcount>50:
			break
			
	if vcount>52:
		message("Timeout:","su 1V0 %.2fv" % adc(OUT_1V0),message_timeout)
		continue

	time.sleep(0.2)
	a=adc(OUT_1V8)
	a=adc(OUT_1V8)
	print a	
	if a<1.8:
		message("Errore:","NO 1V8 %.2fv" % a,message_timeout)
		a=adc(OUT_1V8)	
		continue

	a=adc(OUT_3V3)		
	a=adc(OUT_3V3)		
	if a<3.24:
		message("Errore:","NO 3V3 %.2fv" % adc(OUT_3V3),message_timeout)
		a=adc(OUT_3V3)		
		continue
	
	counter_ok=counter_ok+1	
	message("       OK       ","",message_timeout+1)
