import fox
import time

# Define myled as the led labeled "L1" on the 
# Daisy11 module wired on D2 connector

myled = daisy.Daisy11('D2','L1')
 
while True:
	myled.on()
	time.sleep(0.2)
	myled.off()
	time.sleep(0.2)
