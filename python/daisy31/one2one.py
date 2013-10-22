import serial

#Terra D13 or FOX D1
ser1 = serial.Serial(
	port='/dev/ttyS2', 
	baudrate=9600, 
	timeout=1,
	parity=serial.PARITY_NONE,
	stopbits=serial.STOPBITS_ONE,
	rtscts = None,
	bytesize=serial.EIGHTBITS
)

#Terra D10 or FOX D6
ser2 = serial.Serial(
	port='/dev/ttyS4', 
	baudrate=9600, 
	timeout=1,
	parity=serial.PARITY_NONE,
	stopbits=serial.STOPBITS_ONE,
	rtscts = None,
	bytesize=serial.EIGHTBITS
)    

# This command can be used to query individual or multiple non-volatile parameters
# The requested number of bytes from the specified memory position is returned.
# Example (query of all parameters):
# output1 = chr(0xFF) + chr(0x0A) + chr(0x02) + chr(0x00) + chr(0x80) + chr(0x77)

# Set RF power to 0dBm
output1 = chr(0xFF) + chr(0x09) + chr(0x03) + chr(0x3D) + chr(0x01) + chr(0x02) + chr(0xCB)

# RF broadcast transmission example
# Example string: "Hello World!" preceded by string lenght (12 byte)
output2 = chr(0x0D) + chr(0x48) + chr(0x65) + chr(0x6C) + chr(0x6C) + chr(0x6F) + chr(0x20) + chr(0x57) + chr(0x6F) + chr(0x72) + chr(0x6C) + chr(0x64) + chr(0x21) + chr(0x21)

# Write buffered string stored in output1. MBus connectes to D1
ser1.write(output1)
s = ser1.read(140)         # Wait for 140 char
print "Response from MBus module connected on D1"
print s.encode("hex")

# Write buffered string stored in output2. MBus connectes to D3
ser2.write(output1)
s = ser2.read(140)         # Wait for 140 char
print "Response from MBus module connected on D3"
print s.encode("hex")

# RF Test 1
ser1.write(output2) 
s = ser2.read(40)         # Wait for 40 char
#print s.encode("hex")
print "RF Test 1, From D1 to D3"
print s

# RF Test 2
ser2.write(output2) 
s = ser1.read(40)         # Wait for 40 char
#print s.encode("hex")
print "RF Test 2, From D3 to D1"
print s

ser1.close()
ser2.close()
