import ablib
import time
import sqlite3

#Callback function for pushbutton P1 
def P1_pressed():
	connection = sqlite3.connect('events.sqlite')
	cursor = connection.cursor()
	print "P1 pressed"	
	cursor.execute('insert into events values(datetime("now"),"P1 pressed");')
	connection.commit()
	connection.close()

#Callback function for pushbutton P2 
def P2_pressed():
	connection = sqlite3.connect('events.sqlite')
	cursor = connection.cursor()
	print "P2 pressed"	
	cursor.execute('insert into events values(datetime("now"),"P2 pressed");')
	connection.commit()
	connection.close()

P1 = ablib.Daisy5('D11','P1')
P1.set_edge("rising",P1_pressed)

P2 = ablib.Daisy5('D11','P2')
P2.set_edge("rising",P2_pressed)

#Forever loop
while True:
	time.sleep(10)	
