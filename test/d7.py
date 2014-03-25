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

wincmd = curses.newwin(30, 50, 1, 1) 
wincmd.bkgd(curses.color_pair(2)) 
wincmd.box() 

while True:
	acc=mems.acc_read()
	acc_row=2
	
	wincmd.addstr(acc_row+0, 2, "X: %6d" % (acc["X"])) 
	wincmd.addstr(acc_row+1, 2, "Y: %6d" % (acc["Y"])) 
	wincmd.addstr(acc_row+2, 2, "Z: %6d" % (acc["Z"])) 
	
	gyro=mems.gyro_read()
	gyro_row=acc_row+4
	
	wincmd.addstr(gyro_row+0, 2, "X: %6d" % (gyro["X"])) 
	wincmd.addstr(gyro_row+1, 2, "Y: %6d" % (gyro["Y"])) 
	wincmd.addstr(gyro_row+2, 2, "Z: %6d" % (gyro["Z"])) 

	wincmd.refresh() 
	time.sleep(0.1)

cleanup()
