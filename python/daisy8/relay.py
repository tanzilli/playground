import ablib
import time

RL0 = ablib.Daisy8(connector='D11',id='RL0')
RL1 = ablib.Daisy8(connector='D11',id='RL1')
 
while True:
	RL0.on()
	time.sleep(1)

	RL1.on()
	time.sleep(1)

	RL0.off()
	time.sleep(1)

	RL1.off()
	time.sleep(1)


