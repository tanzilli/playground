import os.path
import time

L0 = 63
L1 = 62
L2 = 61
L3 = 60

class ServoRC():
	offset_pulse = 800
	center_pulse = 1500
	period=20000
	kernel_id=-1
	
	def __init__(self,kernel_id):
		self.kernel_id=kernel_id

		iopath='/sys/class/soft_pwm/pwm' + str(kernel_id)
		if not os.path.exists(iopath): 
			f = open('/sys/class/soft_pwm/export','w')
			f.write(str(kernel_id))
			f.close()

	def setperiod(self,value):
		iopath='/sys/class/soft_pwm/pwm' + str(self.kernel_id)
		if os.path.exists(iopath): 
			f = open(iopath + '/period','w')
			f.write(str(value))
			f.close()

	def setpulse(self,value):
		iopath='/sys/class/soft_pwm/pwm' + str(self.kernel_id)
		if os.path.exists(iopath): 
			f = open(iopath + '/pulse','w')
			f.write(str(value))
			f.close()


	def config(self,period,center_pulse,offset_pulse):
		self.period=period
		self.center_pulse = center_pulse
		self.offset_pulse = offset_pulse

	def move(self,degree):
		pulse=self.center_pulse-self.offset_pulse+((self.offset_pulse/90)*degree)
		self.setperiod(self.period)
		self.setpulse(pulse)
		time.sleep(0.5)	
		self.setperiod(0)


a=ServoRC(63)
a.move(180)


	

