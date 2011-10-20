import time
import thread
import fox
import threading
 
# This is the function that will be executed as a thread  
def check_button(button,led):
	while True:
		if button.pressed():
			led.on()
		else:
			led.off()
		time.sleep(0.1)
 
# Define myled as the led labeled "L1" on the 
# Daisy11 module wired on D2 connector 
myled = fox.Daisy11('D2','L1')


# Define mybutton as the press button labeled "P1" on the 
# Daisy5 module wired on D5 connector 
mybutton = fox.Daisy5('D5','P1')
 
 
# Launch the funcion check_button as a thread
# and pass as arguments the button and led instances  
thread.start_new_thread(check_button,(mybutton,myled))
 
# The main program flow continues and makes the L8 blinking
# to show you that it's running in parallel with the thread 
blinking_led = fox.Daisy11('D2','L8')
 
while True:
	blinking_led.on()
	time.sleep(0.2)
	blinking_led.off()
	time.sleep(0.2)
