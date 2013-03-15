import ablib

d10_module=ablib.Daisy10(port="D10",baudrate=9600,timeout=10)
d10_module.mode("RS485")

d10_module.flushInput()
d10_module.write("Hello World !")

print "Wait %d seconds for something from RS485 bus" % d10_module.timeout
print d10_module.read(20)


