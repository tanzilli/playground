import time
import fox
 
print "Telit ON/OFF"
 
telitRESET = fox.Pin('J6','38','low')
telitON = fox.Pin('J6','37','low')
 
telitON.on()
time.sleep(1)
telitON.off()
