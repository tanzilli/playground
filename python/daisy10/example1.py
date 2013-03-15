import ablib

rs485=ablib.Daisy10(port="D10",baudrate=9600)
rs485.mode("RS485")
rs485.write("Ciao a tutti come va ? \n")

