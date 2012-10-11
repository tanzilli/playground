import ablib
import time

#Create an istance of Daisy2 class called motor1
motor1 = ablib.Daisy2('D5','A')

#Enable the the Texas chip
motor1.enable_on()

#Forever loop
while True:
	# Forward direction
	motor1.set_dir(0)

	#Enable the power over the H-bridges
	motor1.hipower()

	#Send 200 steps (1 complete turn with 1.8 degree by step motor) 
	for i in range(0,200):
		motor1.step_on()

	#Se the low power mode. In this way the Texas chip
	#will send a PWM signal instead of a continuosly
	#current to save power holding the torque
	motor1.lowpower()

	#Wait 2 seconds
	time.sleep(2)


	# Repeat the same operation in the other direction
	motor1.set_dir(1)
	motor1.hipower()
	for i in range(0,200):
		motor1.step_on()

	motor1.lowpower()
	time.sleep(2)

