#!/usr/bin/python

import struct

inputDevice = "/dev/input/event1" #keyboard on my system
inputEventFormat = 'iihhi'
inputEventSize = 16

file = open(inputDevice, "rb") # standard binary file input
event = file.read(inputEventSize)
while event:
	(time1, time2, type, code, value) = struct.unpack(inputEventFormat, event)
	print type,code,value
	event = file.read(inputEventSize)
file.close()
