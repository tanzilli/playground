from time import sleep
from ablib import Pin
  
print "Modem OFF"
 
quectel_power = Pin('W10','LOW')
quectel_power_key = Pin('E10','LOW')

