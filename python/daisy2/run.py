import ablib
import time

motor1 = ablib.Daisy2('D5','low')
motor1.enable_on()

while True:
	for i in range(1,200):
		motor1.step_on()

	motor1.set_dir(0)

	for i in range(1,200):
		motor1.step_on()

	motor1.set_dir(1)

