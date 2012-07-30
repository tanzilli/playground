#!/usr/bin/python
import time
import thread
import threading
import ablib

#Commento di prova 
def check_button(button,led):
	while True:
		if button.pressed():
			led.on()
		else:
			led.off()
		time.sleep(0.1)
 
def timed_led(button,led,delay):
	while True:
		if button.pressed():
			led.on()
			time.sleep(delay)
			led.off()
 
myled = ablib.Daisy11('D2','L1')
mybutton = ablib.Daisy5('D5','P1')
 
myled_2 = ablib.Daisy11('D2','L2')
mybutton_2 = ablib.Daisy5('D5','P2')
 
thread.start_new_thread(check_button,(mybutton,myled))
thread.start_new_thread(timed_led,(mybutton_2,myled_2,5))
 
loop_counter=0
while True:
	print "loop # " , loop_counter
	loop_counter += 1
	time.sleep(1)
