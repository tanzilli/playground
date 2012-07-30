import ablib
import time

#Define which i2c_bus device driver to use
#(normally /dev/i2c-0) 
i2c_bus=0

#Set I2C address configured on the Daisy-22
i2c_address=0x27

#Create an istance of Daisy-22 class 
#to for the gpio lines P0 to P3
P0=ablib.Daisy22(i2c_bus,i2c_address,0)
P1=ablib.Daisy22(i2c_bus,i2c_address,1)
P2=ablib.Daisy22(i2c_bus,i2c_address,2)
P3=ablib.Daisy22(i2c_bus,i2c_address,3)

#Read the P0 line forever
while True:
	if P0.get()==0:
		print "Push button on P0 pressed !"
	if P1.get()==0:
		print "Push button on P1 pressed !"
	if P2.get()==0:
		print "Push button on P2 pressed !"
	if P3.get()==0:
		print "Push button on P3 pressed !"
	time.sleep(0.2)


