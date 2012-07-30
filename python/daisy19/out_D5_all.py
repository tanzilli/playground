import ablib
import time

# Define myled as the led labeled "L1" on the 
# Daisy11 module wired on D2 connector

Out1 = ablib.Daisy19('D5','first','O1')
Out2 = ablib.Daisy19('D5','first','O2')
Out3 = ablib.Daisy19('D5','first','O3')
Out4 = ablib.Daisy19('D5','first','O4')
Out5 = ablib.Daisy19('D5','second','O1')
Out6 = ablib.Daisy19('D5','second','O2')
Out7 = ablib.Daisy19('D5','second','O3')
Out8 = ablib.Daisy19('D5','second','O4')



 
while True:
	Out1.on()
	Out2.on()
	Out3.on()
	Out4.on()
	time.sleep(0.2)
	Out1.off()
	Out2.off()
	Out3.off()
	Out4.off()
	time.sleep(0.2)
	Out5.on()
	Out6.on()
	Out7.on()
	Out8.on()
	time.sleep(0.2)
	Out5.off()
	Out6.off()
	Out7.off()
	Out8.off()
	time.sleep(0.2)
