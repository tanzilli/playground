import acmeboards
import time

kernel_id = acmeboards.get_kernel_id('N','2')
acmeboards.export(kernel_id)
acmeboards.direction(kernel_id,'low')

while True:
	acmeboards.set_value(kernel_id,1)
	time.sleep(1)
	acmeboards.set_value(kernel_id,0)
	time.sleep(1)

