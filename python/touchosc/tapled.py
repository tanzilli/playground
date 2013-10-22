from ablib import Daisy11
from OSC import OSCServer,OSCClient, OSCMessage
from time import sleep
import types

L1=Daisy11("D11","L1")
L2=Daisy11("D11","L2")
L3=Daisy11("D11","L3")
L4=Daisy11("D11","L4")
L5=Daisy11("D11","L5")
L6=Daisy11("D11","L6")
L7=Daisy11("D11","L7")
L8=Daisy11("D11","L8")

server = OSCServer(("0.0.0.0", 8000))

def push1_callback(path, tags, args, source):
	if path=="/7/push1":
	    if args[0]==1.0:
	        L1.on()
	    else:
	        L1.off()

def push2_callback(path, tags, args, source):
	if path=="/7/push2":
	    if args[0]==1.0:
	        L2.on()
	    else:
	        L2.off()

def push3_callback(path, tags, args, source):
	if path=="/7/push3":
	    if args[0]==1.0:
	        L3.on()
	    else:
	        L3.off()

def push4_callback(path, tags, args, source):
	if path=="/7/push4":
	    if args[0]==1.0:
	        L4.on()
	    else:
	        L4.off()

def push5_callback(path, tags, args, source):
	if path=="/7/push5":
	    if args[0]==1.0:
	        L5.on()
	    else:
	        L5.off()

def push6_callback(path, tags, args, source):
	if path=="/7/push6":
	    if args[0]==1.0:
	        L6.on()
	    else:
	        L6.off()

def push7_callback(path, tags, args, source):
	if path=="/7/push7":
	    if args[0]==1.0:
	        L7.on()
	    else:
	        L7.off()

def push8_callback(path, tags, args, source):
	if path=="/7/push8":
	    if args[0]==1.0:
	        L8.on()
	    else:
	        L8.off()

def handle_error(self,request,client_address):
    pass

server.addMsgHandler( "/7/push1",push1_callback)
server.addMsgHandler( "/7/push2",push2_callback)
server.addMsgHandler( "/7/push3",push3_callback)
server.addMsgHandler( "/7/push4",push4_callback)
server.addMsgHandler( "/7/push5",push5_callback)
server.addMsgHandler( "/7/push6",push6_callback)
server.addMsgHandler( "/7/push7",push7_callback)
server.addMsgHandler( "/7/push8",push8_callback)


server.handle_error = types.MethodType(handle_error, server)

while True:
	server.handle_request()

server.close()


