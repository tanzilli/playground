import ablib
import time

motor1 = ablib.Daisy2('D2','A')
motor2 = ablib.Daisy2('D5','B')

motor1.enable()
motor2.enable()

motor1.hipower()
motor2.hipower()

while True:
	motor1.direction(1)
	motor2.direction(0)

	motor1.steps(200)
	motor2.steps(200)

	time.sleep(1)

	motor1.direction(0)
	motor2.direction(1)

	motor1.steps(200)
	motor2.steps(200)

	time.sleep(1)

