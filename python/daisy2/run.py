import ablib
import time

#Create an istance of a Daisy2 class called motor1
#The Daisy2 module is plugged on D5 connector
motor1 = ablib.Daisy2('D5')

#Enable the the Texas chip
motor1.enable()

# Clockwise direction
motor1.direction(1)

#Enable hi-power over the H-bridges
motor1.hipower()

motor1.steps(200)

#Set the low power mode. In this way the Texas chip
#will send a PWM signal instead of a continuosly
#current to save power holding the torque
motor1.lowpower()

#Wait
time.sleep(1)

# Anti-Clockwise direction
motor1.direction(0)
motor1.hipower()

motor1.steps(200)

time.sleep(1)
motor1.disable()

