import posix
import struct
from ctypes import addressof, create_string_buffer, sizeof, string_at
from fcntl import ioctl
from spi_ctypes import *
import time

write_buf=create_string_buffer(50)
read_buf=create_string_buffer(50)

ioctl_arg = spi_ioc_transfer(
		tx_buf=addressof(write_buf),
		rx_buf=addressof(read_buf),
		len=2,
		delay_usecs=0,
		speed_hz=5000000,
		bits_per_word=8,
		cs_change = 0,
)

bits= spi_ioc_transfer(7)

device_name = "/dev/spidev32766.0"
adc_channel=5
print "Read from %s on a/d channel %d" % (device_name,adc_channel)


fd = posix.open(device_name, posix.O_RDWR)
ioctl(fd, SPI_IOC_RD_MODE, " ")
ioctl(fd, SPI_IOC_WR_MODE, struct.pack('I',0))

#Write the A/D channel address and read the value
write_buf[0]=chr(adc_channel*8)
write_buf[1]=chr(0x00)

while True:
	ioctl(fd, SPI_IOC_MESSAGE(1), addressof(ioctl_arg))
	print "Value %d" % (ord(read_buf[1])*256+ord(read_buf[0]))
	time.sleep(1)
	
	
