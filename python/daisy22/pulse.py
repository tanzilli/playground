import ablib
import time

#Define which i2c_bus device driver to use
#(normally /dev/i2c-0) 
i2c_bus=0

#Set I2C address configured on the Daisy-22
i2c_address=0x27

#Create an istance of Daisy-22 class 
#to manage the P0 line
 
P0=ablib.Daisy22(i2c_bus,i2c_address,0)

#Create an istance of Daisy-22 class 
#to manage the P1 line
 
P1=ablib.Daisy22(i2c_bus,i2c_address,1)

#Turn on (1) and off (0) the GPIO line
#each second

#Send a pulse on P0 gpio line 
P0.on()
time.sleep(1)
P0.off()

#Send a pulse on P1 gpio line 
P1.on()
time.sleep(1)
P1.off()

