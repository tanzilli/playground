#Read a pushbutton on Daisy5 module
#using a polling

from ablib import Daisy5
from time import sleep

connector="D12"

button = Daisy5(connector,'P1')

while True:
	if (button.get()):
		print "Pressed" 
        sleep(0.2)

