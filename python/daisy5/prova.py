#!/usr/bin/python

# Test interrupts.

import select, time, ablib
import thread
import threading

def check_button(fd,callback):
	po = select.epoll()
	po.register(fd,select.EPOLLET)
	while True:
		events = po.poll()
		callback()

def tasto_P1():
	print "Tasto P1 premuto"

def tasto_P2():
	print "Tasto P2 rilasciato"

P1=ablib.Daisy5('D11','P1')
P1.set_edge("rising")

P2=ablib.Daisy5('D11','P2')
P2.set_edge("falling")


thread.start_new_thread(check_button,(P1.fd,tasto_P1))
thread.start_new_thread(check_button,(P2.fd,tasto_P2))


i=0
while True:
	time.sleep(1)
	print i
	i=i+1
	pass

