from ablib import Daisy8
from time import sleep

RL0 = Daisy8('D11','first','RL0')
RL1 = Daisy8('D11','first','RL1')
 
while True:
	RL0.on()
	sleep(1)

	RL1.on()
	sleep(1)

	RL0.off()
	sleep(1)

	RL1.off()
	sleep(1)


