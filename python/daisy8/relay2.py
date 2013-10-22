from ablib import Daisy8
from time import sleep

RL0_A = Daisy8('D11','RL0','first')
RL1_A = Daisy8('D11','RL1','first')
RL0_B = Daisy8('D11','RL0','second')
RL1_B = Daisy8('D11','RL1','second')
 
while True:
	RL0_A.on()
	sleep(0.5)

	RL1_A.on()
	sleep(0.5)

	RL0_B.on()
	sleep(0.5)

	RL1_B.on()
	sleep(0.5)

	RL0_A.off()
	sleep(0.5)

	RL1_A.off()
	sleep(0.5)

 	RL0_B.off()
	sleep(0.5)

	RL1_B.off()
	sleep(0.5)
