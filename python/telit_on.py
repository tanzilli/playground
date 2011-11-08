import time
import fox
 
print "Telit ON/OFF"
 
telitON = fox.Pin('J6.37','low')
 
telitON.on()
time.sleep(1)
telitON.off()
