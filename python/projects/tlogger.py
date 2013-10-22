#!/usr/bin/python
import time
import ablib
from pysqlite2 import dbapi2 as sqlite
 
# Read the temperature value from the thermal sensor identified 
# by the id 0000027f8f99. This is a unique ID available on
# /sys/bus/w1/devices  
 
sensor = ablib.DS18B20("0000027f8f99")
sample = sensor.getTemp()
 
# Insert a new record for this sample on the SQLite database
 
connection = sqlite.connect('/var/www/temperatures.sqlite')
cursor = connection.cursor()
cursor.execute('CREATE TABLE IF NOT EXISTS samples (id INTEGER PRIMARY KEY AUTOINCREMENT, date TEXT, time TEXT, value FLOAT)')
cursor.execute('INSERT INTO samples VALUES (null, date("now","localtime"),time("now","localtime"),' + "%.2f" % sample + ')')
connection.commit()
 
print "Temp=%.2f C" % (sensor.getTemp())
