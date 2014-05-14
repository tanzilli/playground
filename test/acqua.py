from ablib import Pin
import time

j1pinlist = [
	 9,
	10,
	11,
	12,
	13,
	14,
	15,
	16,
	17,
	18,
	19,
	20,
	21,
	22,
	23,
	24,
	25,
	26,
	27,
	28,
	29,
	30,
	31,
	32,
	33,
	35,
	36,
	37,
	38,
	39,
	40,
	41,
	42,
	43,
	44,
	45,
	46,
	47,
	48,
	49,
]

j2pinlist = [
	 1,
	 2,
	 3,
	 5,
	 6,
	 7,
	 8,
	 9,
	10,
	11,
	12,
	13,
	14,
	15,
	16,
	17,
	18,
	19,
	23,
	25,
	29,
	31,
	32,
	33,
	34,
	35,
	36,
	37,
	38,
	39,
	40,
	42,
	43,
	44,
	45,
	46,
]

j3pinlist = [
	 5,
	 6,
	 7,
	 8,
	 9,
	10,
	11,
	12,
	13,
	14,
	15,
	16,
	17,
	18,
	19,
	20,
	22,
	23,
	24,
	25,
	26,
	28,
	29,
	30,
	31,
	32,
	33,
	34,
	35,
	36,
	37,
	38,
	39,
	40,
	41,
	42,
	43,
	44,
	45,
	46,
	47,
	48,
	49,
	50,
]

class _GetchUnix:
	def __init__(self):
		import tty, sys
	def __call__(self):
		import sys, tty, termios
		fd = sys.stdin.fileno()
		old_settings = termios.tcgetattr(fd)
		try:
			tty.setraw(sys.stdin.fileno())
			ch = sys.stdin.read(1)
		finally:
			termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
		return ch

getch=_GetchUnix()
while True:

	print ""
	print "Acqua quick test"
	print "----------------------"
	print "1 - All ON"
	print "2 - All OFF"
	print "3 - Left ON"
	print "4 - Right ON"
	print "5 - ON-OFF"
	print "6 - OFF-ON"
	print "q - Quit"
	print "----------------------"

	print "Select: ",
	test_to_run=getch()
	if test_to_run=="q":
		print "Goodbye cruel world !"
		quit()
	print " "

	if test_to_run=="1":
		for ariapin in j1pinlist:
			a = Pin("J1." + str(ariapin),'OUTPUT')
			a.on()

		for ariapin in j2pinlist:
			a = Pin("J2." + str(ariapin),'OUTPUT')
			a.on()

		#J3
		for ariapin in j3pinlist:
			a = Pin("J3." + str(ariapin),'OUTPUT')
			a.on()

	if test_to_run=="2":
		for ariapin in j1pinlist:
			a = Pin("J1." + str(ariapin),'OUTPUT')
			a.off()

		for ariapin in j2pinlist:
			a = Pin("J2." + str(ariapin),'OUTPUT')
			a.off()

		#J3
		for ariapin in j3pinlist:
			a = Pin("J3." + str(ariapin),'OUTPUT')
			a.off()

	if test_to_run=="3":
		for ariapin in j1pinlist:
			a = Pin("J1." + str(ariapin),'OUTPUT')
			if (ariapin % 2)==0:
				a.off()
			else:
				a.on()
		for ariapin in j2pinlist:
			a = Pin("J2." + str(ariapin),'OUTPUT')
			if (ariapin % 2)==0:
				a.off()
			else:
				a.on()
		#J3
		for ariapin in j3pinlist:
			a = Pin("J3." + str(ariapin),'OUTPUT')
			if (ariapin % 2)==0:
				a.off()
			else:
				a.on()

	if test_to_run=="4":
		for ariapin in j1pinlist:
			a = Pin("J1." + str(ariapin),'OUTPUT')
			if (ariapin % 2)==1:
				a.off()
			else:
				a.on()
		for ariapin in j2pinlist:
			a = Pin("J2." + str(ariapin),'OUTPUT')
			if (ariapin % 2)==1:
				a.off()
			else:
				a.on()
		#J3
		for ariapin in j3pinlist:
			a = Pin("J3." + str(ariapin),'OUTPUT')
			if (ariapin % 2)==1:
				a.off()
			else:
				a.on()

	if test_to_run=="5":
		#J1
		flag=0
		for ariapin in j1pinlist:
			if (ariapin % 2)==1:
				a = Pin("J1." + str(ariapin),'OUTPUT')
				if flag==0:
					a.on()
					flag=1
				else:
					a.off()
					flag=0
		flag=0
		for ariapin in j1pinlist:
			if (ariapin % 2)==0:
				a = Pin("J1." + str(ariapin),'OUTPUT')
				if flag==0:
					a.on()
					flag=1
				else:
					a.off()
					flag=0

		#J2
		flag=0
		for ariapin in j2pinlist:
			if (ariapin % 2)==1:
				a = Pin("J2." + str(ariapin),'OUTPUT')
				if flag==0:
					a.on()
					flag=1
				else:
					a.off()
					flag=0
		flag=0
		for ariapin in j2pinlist:
			if (ariapin % 2)==0:
				a = Pin("J2." + str(ariapin),'OUTPUT')
				if flag==0:
					a.on()
					flag=1
				else:
					a.off()
					flag=0

		#J3
		flag=0
		for ariapin in j3pinlist:
			if (ariapin % 2)==1:
				a = Pin("J3." + str(ariapin),'OUTPUT')
				if flag==0:
					a.on()
					flag=1
				else:
					a.off()
					flag=0
		flag=0
		for ariapin in j3pinlist:
			if (ariapin % 2)==0:
				a = Pin("J3." + str(ariapin),'OUTPUT')
				if flag==0:
					a.on()
					flag=1
				else:
					a.off()
					flag=0

	if test_to_run=="6":
		#J1
		flag=0
		for ariapin in j1pinlist:
			if (ariapin % 2)==1:
				a = Pin("J1." + str(ariapin),'OUTPUT')
				if flag==0:
					a.off()
					flag=1
				else:
					a.on()
					flag=0
		flag=0
		for ariapin in j2pinlist:
			if (ariapin % 2)==0:
				a = Pin("J2." + str(ariapin),'OUTPUT')
				if flag==0:
					a.off()
					flag=1
				else:
					a.on()
					flag=0

		#J2
		flag=0
		for ariapin in j2pinlist:
			if (ariapin % 2)==1:
				a = Pin("J2." + str(ariapin),'OUTPUT')
				if flag==0:
					a.off()
					flag=1
				else:
					a.on()
					flag=0
		flag=0
		for ariapin in j2pinlist:
			if (ariapin % 2)==0:
				a = Pin("J2." + str(ariapin),'OUTPUT')
				if flag==0:
					a.off()
					flag=1
				else:
					a.on()
					flag=0

		#J3
		flag=0
		for ariapin in j3pinlist:
			if (ariapin % 2)==1:
				a = Pin("J3." + str(ariapin),'OUTPUT')
				if flag==0:
					a.off()
					flag=1
				else:
					a.on()
					flag=0
		flag=0
		for ariapin in j3pinlist:
			if (ariapin % 2)==0:
				a = Pin("J3." + str(ariapin),'OUTPUT')
				if flag==0:
					a.off()
					flag=1
				else:
					a.on()
					flag=0
