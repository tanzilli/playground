import fox
import time

kernel_id = get_kernel_id("N","1")
export(kernel_id)
direction(kernel_id,'low')

while True:
	set_value(kernel_id,1)
	time.sleep(1)
	set_value(kernel_id,0)
	time.sleep(1)

