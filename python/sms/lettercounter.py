#!/usr/bin/env python
#The original version of this example in available on 
#https://github.com/adammck/pygsm/blob/master/demo.py

import time
from pygsm import GsmModem

class CountLettersApp(object):
	def __init__(self, modem):
		self.modem = modem

	def incoming(self, msg):
		msg.respond("Thanks for those %d characters!" %\
		len(msg.text))

	def serve_forever(self):
		while True:
			print "Checking for message..."
			msg = self.modem.next_message()

			if msg is not None:
				print "Got Message: %r" % (msg)
				self.incoming(msg)

			time.sleep(2)


# all arguments to GsmModem.__init__ are optional, and passed straight
# along to pySerial. for many devices, this will be enough:

Daisy13_on_D1="/dev/ttyS2"

gsm = GsmModem(port=Daisy13_on_D1,baudrate=115200,logger=GsmModem.debug_logger).boot()

print "Waiting for network..."
s = gsm.wait_for_network()

# start the demo app
app = CountLettersApp(gsm)
app.serve_forever()

