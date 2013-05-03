import time, ablib

def pressed():
	print "Ok"

P1=ablib.Daisy5('D11','P1')
P1.set_edge("rising",pressed)

i=0
while True:
	print i
	i=i+1
	time.sleep(0.5)
