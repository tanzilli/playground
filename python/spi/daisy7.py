import posix
import struct
from ctypes import addressof, create_string_buffer, sizeof, string_at
from fcntl import ioctl
from spi_ctypes import *
import time

class StepperDaisyChain():

	"""
	DAISY-2 Stepper motor controller
	http://www.acmesystems.it/DAISY-2-V2
	"""

	fd=None
	nslot=0

	write_buf=create_string_buffer(50)
	read_buf=create_string_buffer(50)

	ioctl_arg = spi_ioc_transfer(
		tx_buf=addressof(write_buf),
		rx_buf=addressof(read_buf),
		len=1,
		delay_usecs=0,
		speed_hz=5000000,
		bits_per_word=8,
		cs_change = 0,
		)

	def __init__(self,device,nslot):
		self.fd = posix.open(device, posix.O_RDWR)
		ioctl(self.fd, SPI_IOC_RD_MODE, " ")
		ioctl(self.fd, SPI_IOC_WR_MODE, struct.pack('I',0))
		self.nslot = nslot

	def nop(self,slot):
		for i in range(0,self.nslot):
			self.write_buf[i]=chr(0x00)
		self.ioctl_arg.len=self.nslot*1
		ioctl(self.fd, SPI_IOC_MESSAGE(1),addressof(self.ioctl_arg))
		print ord(self.read_buf[slot])

	def GetParam(self,slot,param):
		if param>0x1B:
			print "Invalid PARAM"
			return

		for i in range(0,self.nslot):
			self.write_buf[i]=chr(0x20+param)
			
		self.ioctl_arg.len=self.nslot
		ioctl(self.fd, SPI_IOC_MESSAGE(1), addressof(self.ioctl_arg))

		for i in range(0,self.nslot):
			print "%02X" % ord(self.read_buf[i])
			
		for i in range(0,self.nslot):
			self.write_buf[i]=chr(0x00)
			
		self.ioctl_arg.len=self.nslot
		ioctl(self.fd, SPI_IOC_MESSAGE(1), addressof(self.ioctl_arg))

		for i in range(0,self.nslot):
			print "%02X" % ord(self.read_buf[i])

		for i in range(0,self.nslot):
			self.write_buf[i]=chr(0x00)
		
		self.ioctl_arg.len=self.nslot
		ioctl(self.fd, SPI_IOC_MESSAGE(1), addressof(self.ioctl_arg))

		for i in range(0,self.nslot):
			print "%02X" % ord(self.read_buf[i])

class Daisy2():
	daisychain=None
	slot=None
	
	def __init__(self,daisychain,slot):
		if (slot>=daisychain.nslot):
			print "Slot %d is unavailable" % slot
			return
		
		self.daisychain = daisychain
		self.slot = slot

	def GetParam(self,param):
		self.daisychain.GetParam(self.slot,param)

	def nop(self):
		self.daisychain.nop(self.slot)

daisychain = StepperDaisyChain("/dev/spidev32766.0",1)

motA = Daisy2(daisychain,0)
motA.GetParam(0x18)


