import smbus
import time
 
bus = smbus.SMBus(0)
 
for a in range(0,256):
	bus.write_byte_data(0x20,0x00, a)
	time.sleep(0.1)
