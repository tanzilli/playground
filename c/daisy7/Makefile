#CC=arm-linux-gnueabi-g++
CC=g++
CFLAGS=-I. -Wall
LFLAGS=-lrt

OBJSTATIC = gps.o nmeap01.o iduec.o daisysette.o 


all: static  main

%.o: %.c
	$(CC) $(CFLAGS) -c -o $@ $< 

main: main.c 
	$(CC) $(CFLAGS) $(LFLAGS)  $(OBJSTATIC)  main.c -o  main

static: $(OBJSTATIC)
	ar rcs libmain.a $^

clean:
	rm -f *.o
	rm -f libmain.a
	rm -f libmain.so
