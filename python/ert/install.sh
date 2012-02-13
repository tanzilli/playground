#!/bin/sh
cp ert /bin/ert
chmod a+x /bin/ert
cp evdev.py /usr/lib/python2.6
cp evdev.py /usr/lib/python2.5

grep 'ert' /etc/rc.local
if [ $? -eq 1 ]; then
	echo "/bin/ert &" >> /etc/rc.local
fi
