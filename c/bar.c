/*
 * Symbol Barcode Scanner Reader Software
 * Written by Andy Stewart
 * June 5, 2007
 *
 * This program is free software; you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation; either version 2 of the License, or 
 * (at your option) any later version.
 * 
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 * 
 * You should have received a copy of the GNU General Public License
 * along with this program; if not, write to the Free Software
 * Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA 02111-1307 USA
 *
 * Set the debug variable to 1 to get some debug printouts.
 *
 * One must have the Linux kernel sources installed in order for this to compile.
 *
 * To build it:
 * gcc -o bar bar.c
 * 
 * Note: this code was tested on Linux kernel rev. 2.6.32 (FOX Board G20)
 *
 */

#include <stdio.h>

#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>
#include "string.h"

#include <linux/input.h>

/* defined at the end of this file */
char cvt_ev_char(int);      
void debug_rcvd_event(struct input_event *);

#define MAX_IN_SIZE 30

main(int argc, char *argv[]) {

  int debug = 0;                /* set this to 1 to get debug info */

  struct input_event ev[64];    /* each scan causes more than one event...get them all */

  int fd = -1;                  /* file descriptor for the scanner device */
  int bytes_read = 0;           /* number of bytes read by the read function */
  int i;                        /* loop variable */
  char scanner_in[30];          /* set this bigger if scanned input is more than 30 characters */
  char scan_char;               /* this holds one char at a time...will be concatenated into scanner_in[] */
  int wr_ptr = 0;               /* points into scanner_in so we know where to put the next scan_char */

  printf("Go ahead and scan something - press ctrl_C when finished.\n");
  printf("Look for printouts which say: Input from Scanner\n");
  printf("Ignore other printouts\n");

  /* The device interface can be found in /dev/input/by-id/*Symbol*, which should be a link
   * to /dev/input/eventN, where N is some number.  One may need to adjust the permissions of the
   * eventN file.
   *
   * Yeah, I know it sucks for me to have hardcoded this value...sorry, I was too lazy to compute it.
   */

  if ((fd = open("/dev/input/event1", O_RDONLY)) < 0) {
    printf("Error opening file descriptor - do you have sufficient permission? Maybe it is incorrectly hardcoded - check the source. Exiting.\n");
    return -1;
  }

  while (1) {
    bytes_read = read(fd, &ev, sizeof(struct input_event) * 64);

    if (bytes_read < 0) {
      printf("ERROR: can't properly read from device\n");
      return -1;
    }

    for (i=0; i < (int) (bytes_read / sizeof(struct input_event)); i++) {

      /* Look for a "key press" event */
      if ((ev[i].type == EV_KEY) && (ev[i].value == 1)) {

	if (ev[i].code != KEY_LEFTSHIFT) {
	  scan_char = cvt_ev_char(ev[i].code);         /* Extract the character from the event */
	
	  if (debug) {
	    debug_rcvd_event(&ev[i]);
	    printf("Scan char: %c\n", scan_char);
	  }

	  if (ev[i].code != KEY_ENTER) {
	    scanner_in[wr_ptr++] = scan_char;
	  }
	  else {
	    scanner_in[wr_ptr] = '\0';
	    printf("Input from Scanner: \"%s\"\n", scanner_in);
	    wr_ptr = 0;
	  }

	} /* if (ev[i].code ...) */

      } /* if ((ev[i].type.....)) */
      
    } /* for (i=0...) */

  } /* while (1) */

  close(fd);

} /* main */

/*
 * cvt_ev_char: convert the code in the "keyboard" event to an ASCII character
 *              The character definitions came from /usr/include/linux/input.h
 *              Assumption is that barcodes can only have 0-9, A-Z so other
 *              codes have been removed from the list below.
 * 
 */

char cvt_ev_char(int foo) {

  char bar;

  switch (foo) {
    case KEY_0: bar = '0'; break;
    case KEY_1: bar = '1'; break;
    case KEY_2: bar = '2'; break;
    case KEY_3: bar = '3'; break;
    case KEY_4: bar = '4'; break;
    case KEY_5: bar = '5'; break;
    case KEY_6: bar = '6'; break;
    case KEY_7: bar = '7'; break;
    case KEY_8: bar = '8'; break;
    case KEY_9: bar = '9'; break;

    case KEY_A: bar = 'A'; break;
    case KEY_B: bar = 'B'; break;
    case KEY_C: bar = 'C'; break;
    case KEY_D: bar = 'D'; break;
    case KEY_E: bar = 'E'; break;
    case KEY_F: bar = 'F'; break;
    case KEY_G: bar = 'G'; break;
    case KEY_H: bar = 'H'; break;
    case KEY_I: bar = 'I'; break;
    case KEY_J: bar = 'J'; break;
    case KEY_K: bar = 'K'; break;
    case KEY_L: bar = 'L'; break;
    case KEY_M: bar = 'M'; break;
    case KEY_N: bar = 'N'; break;
    case KEY_O: bar = 'O'; break;
    case KEY_P: bar = 'P'; break;
    case KEY_Q: bar = 'Q'; break;
    case KEY_R: bar = 'R'; break;
    case KEY_S: bar = 'S'; break;
    case KEY_T: bar = 'T'; break;
    case KEY_U: bar = 'U'; break;
    case KEY_V: bar = 'V'; break;
    case KEY_W: bar = 'W'; break;
    case KEY_X: bar = 'X'; break;
    case KEY_Y: bar = 'Y'; break;
    case KEY_Z: bar = 'Z'; break;

    case KEY_ENTER: bar = '\n'; break;

    default: bar = '?';

  }

  return bar;

}

void debug_rcvd_event(struct input_event *ev) {

  char type_str[15];

  switch (ev->type) {
    case EV_SYN:  strcpy(type_str, "EV_SYN"); break;
    case EV_KEY:  strcpy(type_str, "EV_KEY"); break;
    case EV_REL:  strcpy(type_str, "EV_REL"); break;
    case EV_ABS:  strcpy(type_str, "EV_ABS"); break;
    case EV_MSC:  strcpy(type_str, "EV_MSC"); break;
    case EV_SW:   strcpy(type_str, "EV_SW"); break;
    case EV_LED:  strcpy(type_str, "EV_LED"); break;
    case EV_SND:  strcpy(type_str, "EV_SND"); break;
    case EV_REP:  strcpy(type_str, "EV_REP"); break;
    case EV_FF:   strcpy(type_str, "EV_FF"); break;
    case EV_PWR:  strcpy(type_str, "EV_PWR"); break;
    case EV_MAX:  strcpy(type_str, "EV_MAX"); break;

    case EV_FF_STATUS: strcpy(type_str, "EV_FF_STATUS"); break;
	    
    default: strcpy(type_str, "UNK");
      
  }

  printf("Event: time %ld.%06ld, type %s, code %d, value %d\n",
	 ev->time.tv_sec, ev->time.tv_usec, type_str,
	 ev->code, ev->value);

}


