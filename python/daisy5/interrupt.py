#Read a pushbutton on Daisy5 module
#using the interrupt

from time import sleep
from ablib import Daisy5

def pressed():
	print "Pressed"

P1=Daisy5('D12','P1')
P1.set_edge("rising",pressed)

#Unusefull forever loop :-)
i=0
while True:
	print i
	i=i+1
	sleep(0.5)
