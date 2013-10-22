#!/bin/sh
while true
do 
	ps -eo pcpu,pid,user,args | sort -k 1 -r | head -10 >> logfile.txt
	echo "\n" >> logfile.txt
	sleep 60
done
