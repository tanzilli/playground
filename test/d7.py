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

winacc = curses.newwin(8, 20, 1, 1) 
winacc.bkgd(curses.color_pair(2)) 
winacc.addstr(1, 2, "Accellerometer")  
winacc.box() 

wingyro = curses.newwin(8, 20, 1, 22) 
wingyro.bkgd(curses.color_pair(2)) 
wingyro.addstr(1, 2, "Gyroscope") 
wingyro.box() 

wingps = curses.newwin(8, 41, 10, 1) 
wingps.bkgd(curses.color_pair(2)) 
wingps.addstr(1, 2, "GPS") 
wingps.box() 

while True:
	acc=mems.acc_read()
	gyro=mems.gyro_read()
	gps=mems.gps_read()

	winacc.addstr(3, 2, "X: %6d" % acc["X"]) 
	winacc.addstr(4, 2, "Y: %6d" % acc["Y"]) 
	winacc.addstr(5, 2, "Z: %6d" % acc["Z"]) 
	
	wingyro.addstr(3, 2, "X: %6d" % gyro["X"]) 
	wingyro.addstr(4, 2, "Y: %6d" % gyro["Y"]) 
	wingyro.addstr(5, 2, "Z: %6d" % gyro["Z"]) 

	wingps.addstr(3, 2, " Latitude: %f" % gps["latitude"])
	wingps.addstr(4, 2, "Longitude: %f" % gps["longitude"]) 

	winacc.refresh() 
	wingyro.refresh() 
	wingps.refresh() 
	time.sleep(0.1)

cleanup()
