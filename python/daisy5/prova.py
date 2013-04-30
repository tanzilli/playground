#!/usr/bin/python

# Test interrupts.

import select, time, ablib
import thread
import threading

connector = 'D12'

led = [
	ablib.Daisy11(connector,'L1'),
	ablib.Daisy11(connector,'L2'),
	ablib.Daisy11(connector,'L3'),
	ablib.Daisy11(connector,'L4'),
	ablib.Daisy11(connector,'L5'),
	ablib.Daisy11(connector,'L6'),
	ablib.Daisy11(connector,'L7'),
	ablib.Daisy11(connector,'L8')
	]

rolling_on=True

def check_button(fd,callback):
	po = select.epoll()
	po.register(fd,select.EPOLLET)
	while True:
		events = po.poll()
		callback()

def start():
	global rolling_on
	print "Start"
	rolling_on=True

def stop():
	global rolling_on
	print "Stop"
	rolling_on=False

P1=ablib.Daisy5('D11','P1')
P1.set_edge("rising")

P2=ablib.Daisy5('D11','P2')
P2.set_edge("rising")


thread.start_new_thread(check_button,(P1.fd,start))
thread.start_new_thread(check_button,(P2.fd,stop))


i=0
while True:
	for i in range (0,8):
		while rolling_on==False:
			pass
		led[i].on()
		time.sleep(0.1)
 
	for i in range (0,8):
		while rolling_on==False:
			pass
		led[i].off()
		time.sleep(0.1)

