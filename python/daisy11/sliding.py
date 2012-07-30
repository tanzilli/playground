import ablib
import time
 
# Daisy connector on which is wired the
# Daisy11 module
connector = 'D2'
 
# Create a list istances for all the leds
led = [
	ablib.Daisy11(connector,'L1'),
	ablib.Daisy11(connector,'L2'),
	ablib.Daisy11(connector,'L3'),
	ablib.Daisy11(connector,'L4'),
	ablib.Daisy11(connector,'L5'),
	ablib.Daisy11(connector,'L6'),
	ablib.Daisy11(connector,'L7'),
	ablib.Daisy11(connector,'L8')
	]
 
while True:                        # Forever loop
	for i in range (0,8):      # Scan and turn on all the leds 
		led[i].on()        # each 100 mS
		time.sleep(0.1)
 
	for i in range (0,8):      # Scan and turn off all the leds 
		led[i].off()       # each 100 mS
		time.sleep(0.1)
