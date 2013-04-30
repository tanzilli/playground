#!/usr/bin/python

# Test interrupts.

import select, time, ablib

P1=ablib.Daisy5('D11','P1')
P1.set_edge("both")

#while True:
#	if (P1.pressed()):
#		print "P1 pressed" 

po = select.epoll()
po.register(P1.fd,select.EPOLLET)

t1 = time.time()
while True:
	events = po.poll()
	print "falling edge"
