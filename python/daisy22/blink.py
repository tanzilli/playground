import fox
import time

#P0 out on Daisy-22 

i2c_bus=0
i2c_address=0x27
 
P0=fox.Daisy22(i2c_bus,i2c_address,0)

while True:
	P0.on()
	time.sleep(1)
	P0.off()
	time.sleep(1)

