from ablib import Daisy11
from time import sleep

myled = Daisy11('D11','L1')
 
while True:
	myled.on()
	sleep(0.2)
	myled.off()
	sleep(0.2)
