#!/usr/bin/python
#Factory test for Daisy-9 boards
import ablib
import time
import os

TXD3 = ablib.Pin("D10","2","high")
RXD3 = ablib.Pin("D10","3","in")
RTS3 = ablib.Pin("D10","4","high")
CTS3 = ablib.Pin("D10","5","in")

TXD1 = ablib.Pin("D13","2","high")
RXD1 = ablib.Pin("D13","3","in")
RTS1 = ablib.Pin("D13","4","high")
CTS1 = ablib.Pin("D13","5","in")


TXD3.on()
if RXD1.get_value()==0:
	print "Error TXD3->RXD1"
TXD3.off()
if RXD1.get_value()==1:
	print "Error TXD3->RXD1"

TXD1.on()
if RXD3.get_value()==0:
	print "Error TXD1->RXD3"
TXD1.off()
if RXD3.get_value()==1:
	print "Error TXD1->RXD3"

RTS3.on()
if CTS1.get_value()==0:
	print "Error RTS3->CTS1"
RTS3.off()
if CTS1.get_value()==1:
	print "Error RTS3->CTS1"

RTS1.on()
if CTS3.get_value()==0:
	print "Error RTS1->CTS3"
RTS1.off()
if CTS3.get_value()==1:
	print "Error RTS1->CTS3"
