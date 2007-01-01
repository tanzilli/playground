from ablib import Daisy11
from OSC import OSCServer,OSCClient, OSCMessage
from time import sleep
import sys
import types

# Daisy connector on which is wired the
# Daisy11 module
connector = 'D11'
 
# Create a list istances for all the leds
led = [
	Daisy11(connector,'L1'),
	Daisy11(connector,'L2'),
	Daisy11(connector,'L3'),
	Daisy11(connector,'L4'),
	Daisy11(connector,'L5'),
	Daisy11(connector,'L6'),
	Daisy11(connector,'L7'),
	Daisy11(connector,'L8')
]

server = OSCServer( ("0.0.0.0", 8000) )
client = OSCClient()
client.connect( ("192.168.1.59", 9000) )

def handle_timeout(self):
	print ("Timeout")

server.handle_timeout = types.MethodType(handle_timeout, server)

def fader_callback(path, tags, args, source):
	print ("path", path) 
	print ("args", args) 
	print ("source", source) 

	value=int(args[0]*10)	
	if value>1:
		led[0].on()
	if value>2:
		led[1].on()
	if value>3:
		led[2].on()
	if value>4:
		led[3].on()
	if value>5:
		led[4].on()
	if value>6:
		led[5].on()
	if value>7:
		led[6].on()
	if value>8:
		led[7].on()

	if value<1:
		led[0].off()
	if value<2:
		led[1].off()
	if value<3:
		led[2].off()
	if value<4:
		led[3].off()
	if value<5:
		led[4].off()
	if value<6:
		led[5].off()
	if value<7:
		led[6].off()
	if value<8:
		led[7].off()


	msg=OSCMessage("/1/rotary1")
	msg.append(args);
	client.send(msg)


server.addMsgHandler( "/1/fader1",fader_callback)
server.addMsgHandler( "/1/push1",rele_callback)

while True:
	server.handle_request()

server.close()


