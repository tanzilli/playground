import fox
import time

#Define the istance P0 as a GPIO line 0
#on a Daisy-22 with all the address dip switches  
#at the OFF position (I2C address = 0x27)  

i2c_bus=0
i2c_address=0x27
 
P0=fox.Daisy22(i2c_bus,i2c_address,0)

#Turn on (1) and off (0) the GPIO line
#each second

while True:
	P0.on()
	time.sleep(1)
	P0.off()
	time.sleep(1)

