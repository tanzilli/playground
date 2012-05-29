import smbus
import time
 
bus = smbus.SMBus(0)
 
for a in range(0,256):
	bus.write_byte(0x20,a)
	time.sleep(0.1)
