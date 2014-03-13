from time import sleep
import ablib
 
print "Modem ON"
 
quectel_power = ablib.Pin('W10','HIGH')
quectel_power_key = ablib.Pin('E10','LOW')

quectel_power_key.on()
sleep(1)
quectel_power_key.off()
