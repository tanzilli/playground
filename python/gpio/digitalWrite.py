from ablib import Pin
from time import sleep
 
line = Pin('N20','OUTPUT')

while True:
	sleep(0.2)
	line.digitalWrite('HIGH')
	sleep(0.2)
	line.digitalWrite('LOW')
