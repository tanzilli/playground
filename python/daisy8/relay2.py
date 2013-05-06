import ablib
import time

RL0_A = ablib.Daisy8(connector='D11',id='RL0')
RL1_A = ablib.Daisy8(connector='D11',id='RL1')
RL0_B = ablib.Daisy8(connector='D11',id='RL0',position='second')
RL1_B = ablib.Daisy8(connector='D11',id='RL1',position='second')
 
while True:
	RL0_A.on()
	time.sleep(0.5)

	RL1_A.on()
	time.sleep(0.5)

	RL0_B.on()
	time.sleep(0.5)

	RL1_B.on()
	time.sleep(0.5)

	RL0_A.off()
	time.sleep(0.5)

	RL1_A.off()
	time.sleep(0.5)

 	RL0_B.off()
	time.sleep(0.5)

	RL1_B.off()
	time.sleep(0.5)
