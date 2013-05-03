import ablib
import time

def P1_rising():
	print "P1 rising (pressed)"

def P2_falling():
	print "P2 falling (released)"

def P3_both():
	print "P3 both (state changes)"

P1=ablib.Daisy5('D11','P1')
P1.set_edge("rising",P1_rising)

P2=ablib.Daisy5('D11','P2')
P2.set_edge("falling",P2_falling)

P2=ablib.Daisy5('D11','P3')
P2.set_edge("both",P3_both)

i=0
while True:
	print i
	i=i+1
	time.sleep(0.5)
