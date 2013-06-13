#!/bin/bash

microsd_format() {
	while true; do
		echo "Your are formatting" a $microsd_size"GB microSD";
		read -p "Are you sure to continue ? " yn
		case $yn in
			[Yy]* ) ;;
			[Nn]* ) return;;
			* ) echo "Please answer yes or no.";;
		esac

		#Check if exist the /dev/sdb1
		if [ -b /dev/sdb1 ]
		then
		    	echo The /dev/sdb1 exists
		else
		    	echo /dev/sdb1 not found !
			return
		fi


	done
}

fill_menu() {
	echo "Fill" $options "contents on a" $microsd_size "microSD";
}


while true; do
	if [ -b /dev/sdb ]
	then
		microsd_size=$(df -h --total /dev/sdb* | grep "total" | awk '{print $2}' | tr -dc '[0-9.]')

		echo ""
		echo "------------------------------------";
		echo " MICROSD MAKER                      ";
		echo " MicroSD size=" $microsd_size
		echo ""
		echo " Select what to do (ctrl-c to exit) "
		echo "------------------------------------";
		echo ""

		select options in "Format" "Terra" "Aria128" "Aria256" "Fox"; do
		    case $options in
			Format )  microsd_format; return;;
			Terra )   fill_menu; return;;
			Aria128 ) fill_menu; return;;
			Aria256 ) fill_menu; return;;
			Fox )     fill_menu; return;;
		    esac
		done
		return
	else
	    	echo microSD card not found !
	    	echo Insert a microSD card and try again
		return
	fi
done




