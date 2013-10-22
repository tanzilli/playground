#!/usr/bin/python
#Factory test for Daisy-1 boards

import ablib
import time
import serial
import sys
import select
import thread
import threading


def slide(kid_dictionary,a):
	while True:
		for key in sorted(kid_dictionary.iterkeys()):
			if kid_dictionary[key]!=0:
				ablib.export(kid_dictionary[key])
				ablib.direction(kid_dictionary[key],"out")
				ablib.set_value(kid_dictionary[key],0)

		for key in sorted(kid_dictionary.iterkeys()):
			if kid_dictionary[key]!=0:
				ablib.set_value(kid_dictionary[key],1)
				time.sleep(0.1)
				ablib.set_value(kid_dictionary[key],0)
				time.sleep(0.01)

kid_dictionary=ablib.D1_kernel_ids
thread.start_new_thread(slide,(kid_dictionary,1))
kid_dictionary=ablib.D2_kernel_ids
thread.start_new_thread(slide,(kid_dictionary,1))
kid_dictionary=ablib.D3_kernel_ids
thread.start_new_thread(slide,(kid_dictionary,1))
kid_dictionary=ablib.D4_kernel_ids
thread.start_new_thread(slide,(kid_dictionary,1))
kid_dictionary=ablib.D5_kernel_ids
thread.start_new_thread(slide,(kid_dictionary,1))
kid_dictionary=ablib.D6_kernel_ids
thread.start_new_thread(slide,(kid_dictionary,1))
kid_dictionary=ablib.D7_kernel_ids
thread.start_new_thread(slide,(kid_dictionary,1))
kid_dictionary=ablib.D8_kernel_ids
thread.start_new_thread(slide,(kid_dictionary,1))

while True:
	pass
