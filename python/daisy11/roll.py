from ablib import Daisy11
from time import sleep
 
connector = 'D11'
 
# Create a list istances for all the leds
led = [
	Daisy11(connector,'L1'),
	Daisy11(connector,'L2'),
	Daisy11(connector,'L3'),
	Daisy11(connector,'L4'),
	Daisy11(connector,'L5'),
	Daisy11(connector,'L6'),
	Daisy11(connector,'L7'),
	Daisy11(connector,'L8')
]
 
while True: 
    # Scan and turn on all the leds 
    # each 100 mS
	for i in range (0,8):  
		led[i].on()        
		sleep(0.1)
    
    # Scan and turn off all the leds 
    # each 100 mS
	for i in range (0,8):      
		led[i].off()       
		sleep(0.1)
