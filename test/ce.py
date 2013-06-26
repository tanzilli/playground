import ablib
import time
import serial
import sys
import os
import subprocess

def fatal_error(message):
	print "Error: ", message
	lcd.clear()
	lcd.setcurpos(0,0)
	lcd.putstring("Error:")
	lcd.setcurpos(0,1)
	lcd.putstring(message)
	sys.exit(1)


subprocess.call("umount /dev/sda1 2> /dev/null",shell=True,stdout=None,stderr=None)
subprocess.call("umount /dev/sdb1 2> /dev/null",shell=True,stdout=None,stderr=None)
subprocess.call("umount /dev/sdc1 2> /dev/null",shell=True,stdout=None,stderr=None)


lcd = ablib.Daisy24(0)
lcd.backlighton()
lcd.putstring("CE Test Bench")
time.sleep(0.1)


#Check if the usbkeys are plugged
if os.path.exists("/dev/sda")==False:
	fatal_error("No /dev/sda")	

if os.path.exists("/dev/sdb")==False:
	fatal_error("No /dev/sdb")	

if os.path.exists("/dev/sdc")==False:
	fatal_error("No /dev/sdc")
	
#Check if the mount directories exist
#if not create them
if os.path.exists("/media/usbkey_a")==False:
	subprocess.Popen(["mkdir","/media/usbkey_a"])

if os.path.exists("/media/usbkey_b")==False:
	subprocess.Popen(["mkdir","/media/usbkey_b"])

if os.path.exists("/media/usbkey_c")==False:
	subprocess.Popen(["mkdir","/media/usbkey_c"])

subprocess.call("mount -t vfat /dev/sda1 /media/usbkey_a",shell=True,stdout=None,stderr=None)
subprocess.call("mount -t vfat /dev/sdb1 /media/usbkey_b",shell=True,stdout=None,stderr=None)
subprocess.call("mount -t vfat /dev/sdc1 /media/usbkey_c",shell=True,stdout=None,stderr=None)

counter=0
lcd.clear()
while True:
	lcd.setcurpos(0,0)
	lcd.putstring("Write # %4d" % counter)
	subprocess.call("cp ce.py /media/usbkey_a",shell=True,stdout=None,stderr=None)
	subprocess.call("cp ce.py /media/usbkey_b",shell=True,stdout=None,stderr=None)
	subprocess.call("cp ce.py /media/usbkey_c",shell=True,stdout=None,stderr=None)
	subprocess.call("sync",shell=True,stdout=None,stderr=None)
	time.sleep(0.5)

	lcd.setcurpos(0,0)
	lcd.putstring("Read  # %4d" % counter)
	subprocess.call("cp /media/usbkey_a/ce.py dummy_a",shell=True,stdout=None,stderr=None)
	subprocess.call("cp /media/usbkey_b/ce.py dummy_b",shell=True,stdout=None,stderr=None)
	subprocess.call("cp /media/usbkey_c/ce.py dummy_c",shell=True,stdout=None,stderr=None)
	subprocess.call("sync",shell=True,stdout=None,stderr=None)
	time.sleep(0.5)

	lcd.setcurpos(0,0)
	lcd.putstring("Del   # %4d" % counter)
	subprocess.call("rm /media/usbkey_a/ce.py",shell=True,stdout=None,stderr=None)
	subprocess.call("rm /media/usbkey_b/ce.py",shell=True,stdout=None,stderr=None)
	subprocess.call("rm /media/usbkey_c/ce.py",shell=True,stdout=None,stderr=None)
	subprocess.call("sync",shell=True,stdout=None,stderr=None)
	counter=counter+1	
	time.sleep(0.5)
	


