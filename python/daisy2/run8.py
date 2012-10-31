import ablib
import time

#Create the istances for any Daisy2 module
motor1 = ablib.Daisy2('D2')
motor2 = ablib.Daisy2('D2','B')
motor3 = ablib.Daisy2('D3')
motor4 = ablib.Daisy2('D3','B')
motor5 = ablib.Daisy2('D5')
motor6 = ablib.Daisy2('D5','B')
motor7 = ablib.Daisy2('D6')
motor8 = ablib.Daisy2('D7')

#Select the low-power mode
motor1.lowpower()
motor2.lowpower()
motor3.lowpower()
motor4.lowpower()
motor5.lowpower()
motor6.lowpower()
motor7.lowpower()
motor8.lowpower()

#Enable the the Texas chip
motor1.enable_on()
motor2.enable_on()
motor3.enable_on()
motor4.enable_on()
motor5.enable_on()
motor6.enable_on()
motor7.enable_on()
motor8.enable_on()

while True:
	motor1.set_dir(0)
	motor2.set_dir(1)
	motor3.set_dir(0)
	motor4.set_dir(1)
	motor5.set_dir(0)
	motor6.set_dir(1)
	motor7.set_dir(0)
	motor8.set_dir(1)

	motor1.steps(200)
	motor2.steps(200)
	motor3.steps(200)
	motor4.steps(200)
	motor5.steps(200)
	motor6.steps(200)
	motor7.steps(200)
	motor8.steps(200)
	time.sleep(0.5)

	motor1.set_dir(1)
	motor2.set_dir(0)
	motor3.set_dir(1)
	motor4.set_dir(0)
	motor5.set_dir(1)
	motor6.set_dir(0)
	motor7.set_dir(1)
	motor8.set_dir(0)

	motor1.steps(200)
	motor2.steps(200)
	motor3.steps(200)
	motor4.steps(200)
	motor5.steps(200)
	motor6.steps(200)
	motor7.steps(200)
	motor8.steps(200)
	time.sleep(0.5)

