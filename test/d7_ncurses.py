import curses
import atexit 
import ablib
import time

def cleanup(): 
     curses.nocbreak() 
     stdscr.keypad(0) 
     curses.echo() 
     curses.endwin() 

mems=ablib.Daisy7()
#while True:
#	gyro=mems.gyro_read()
#	print "X=%6d Y=%6d Z=%6d" % (gyro["X"],gyro["Y"],gyro["Z"])
#	time.sleep(0.5)

atexit.register(cleanup) 

stdscr = curses.initscr()
curses.noecho() 
curses.cbreak() 
stdscr.keypad(1) 

curses.start_color() 
curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLUE) 
curses.init_pair(2, curses.COLOR_YELLOW, curses.COLOR_BLACK) 

stdscr.bkgd(curses.color_pair(1)) 
stdscr.refresh() 

winacc = curses.newwin(7, 20, 1, 1) 
winacc.bkgd(curses.color_pair(2)) 
winacc.addstr(1, 2, "ACCELLEROMETER")  

wingyro = curses.newwin(7, 20, 1, 22) 
wingyro.bkgd(curses.color_pair(2)) 
wingyro.addstr(1, 2, "GYROSCOPE") 

wincompass = curses.newwin(7, 20, 1, 43) 
wincompass.bkgd(curses.color_pair(2)) 
wincompass.addstr(1, 2, "COMPASS") 

wingps = curses.newwin(6, 41, 9, 1) 
wingps.bkgd(curses.color_pair(2)) 
wingps.addstr(1, 2, "GPS") 

while True:
	(acc_x,acc_y,acc_z)=mems.acc_getAxes()
	(gyro_x,gyro_y,gyro_z)=mems.gyro_getAxes()
	(compass_x,compass_y,compass_z)=mems.compass_getAxes()
	(gps_latitude,gps_longitude)=mems.gps_getCoordinates()

	winacc.addstr(3, 2, "X: %6d" % acc_x) 
	winacc.addstr(4, 2, "Y: %6d" % acc_y) 
	winacc.addstr(5, 2, "Z: %6d" % acc_z) 
	
	wingyro.addstr(3, 2, "X: %6d" % gyro_x) 
	wingyro.addstr(4, 2, "Y: %6d" % gyro_y) 
	wingyro.addstr(5, 2, "Z: %6d" % gyro_z) 

	wincompass.addstr(3, 2, "X: %6d" % compass_x) 
	wincompass.addstr(4, 2, "Y: %6d" % compass_y) 
	wincompass.addstr(5, 2, "Z: %6d" % compass_z) 

	wingps.addstr(3, 2, " Latitude: %f" % gps_latitude)
	wingps.addstr(4, 2, "Longitude: %f" % gps_longitude) 

	winacc.refresh() 
	wingyro.refresh() 
	wincompass.refresh() 
	wingps.refresh() 
	time.sleep(0.1)

cleanup()
