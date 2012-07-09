import fox
import time

kernel_id = fox.get_kernel_id('N','2')
fox.export(kernel_id)
fox.direction(kernel_id,'low')

while True:
	fox.set_value(kernel_id,1)
	time.sleep(1)
	fox.set_value(kernel_id,0)
	time.sleep(1)

