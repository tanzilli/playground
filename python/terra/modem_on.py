from time import sleep
from ablib import Pin
 
print "Modem ON"
 
quectel_power = Pin('W10','HIGH')
quectel_power_key = Pin('E10','LOW')

quectel_power_key.on()
sleep(1)
quectel_power_key.off()

