import time

spidev='/dev/spidev0.0'

while True:
	for i in range(0,1024):
		for ch in range(0,4):
			word=(ch<<14)|(i<<2)
			msb=word>>8
			lsb=word&0x00FF
			f = open(spidev,'wb')
			f.write(chr(msb)+chr(lsb))
			f.close()
