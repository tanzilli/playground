/* ----------------------------------------------------------------------------
 * fast_io_c_example - Example Program for AriaG25 board to send fast data 
 *                     through AriaG25 Port C 
 *
 * Copyright (c) 2012-2013 Roberto Asquini.
 * All rights reserved.
 *
 * FastIO_C_example is based on the work of Douglas Gilbert for its mem2io.c
 *        for accessing input output register of the CPU from userspace  
 *        compile with: gcc fast_io_c_example.c  -o fast_io_c_example.o
 *		  run with:     ./fast_io_c_example.o
 * 
 * http://www.acmesystems.it
 * Roberto Asquini - asquini@acmesystems.it
 *
 * DISCLAIMER: THIS SOFTWARE IS PROVIDED "AS IS" IN THE SAME 
 * TERMS OF THE ORIGINAL DISCLAIMER LISTED BELOW.
 * PLAYING DIRECTLY WITH CPU REGISTER CAN RESULT IN UNPREDICTABLE RESULTS
 * AND CAN EVEN RESULT IN DAMAGE OF THE CPU AND/OR THE ATTACHED HARDWARE.
 * ----------------------------------------------------------------------------
 */

/*
 * Copyright (c) 2010-2012 Douglas Gilbert.
 * All rights reserved.
 *
 * Redistribution and use in source and binary forms, with or without
 * modification, are permitted provided that the following conditions
 * are met:
 * 1. Redistributions of source code must retain the above copyright
 *    notice, this list of conditions and the following disclaimer.
 * 2. Redistributions in binary form must reproduce the above copyright
 *    notice, this list of conditions and the following disclaimer in the
 *    documentation and/or other materials provided with the distribution.
 * 3. The name of the author may not be used to endorse or promote products
 *    derived from this software without specific prior written permission.
 *
 * THIS SOFTWARE IS PROVIDED BY THE AUTHOR AND CONTRIBUTORS ``AS IS'' AND
 * ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
 * IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
 * ARE DISCLAIMED.  IN NO EVENT SHALL THE AUTHOR OR CONTRIBUTORS BE LIABLE
 * FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
 * DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS
 * OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION)
 * HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
 * LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY
 * OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF
 * SUCH DAMAGE.
 *
 */


#include <stdio.h>     
#include <stdlib.h>     
#include <ctype.h>     
#include <string.h>     
#include <unistd.h>    
#include <sys/mman.h>    
#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <errno.h>
#include <time.h>
#include <math.h>


#define DEV_MEM "/dev/mem"
#define MAP_SIZE 4096   /* needs to be a power of 2! */
#define MAP_MASK (MAP_SIZE - 1)

// addresses of interesting physical Port C registers 
#define PIOC_OER  0xfffff810   // (Wr) PIO Output Enable Register -> 1 to the bit that has to be put in output
#define PIOC_ODR  0xfffff814   // (Wr) PIO Output Disable Register -> 1 to the bit that has to be put in input
#define PIOC_SODR 0xfffff830   // (Wr) PIO Set Output Data Register -> 1 to the output bit that has to be set 
#define PIOC_CODR 0xfffff834   // (Wr) PIO Clear Output Data Register -> 1 to the output bit that has to be cleared
#define PIOC_ODSR 0xfffff838   // (Rd) PIO Output Data Status Register : to read the output status of the PortC pins
#define PIOC_PDSR 0xfffff83C   // (Rd) PIO Pin Data Status Register _ to read the status of the PortC input pins

int mem_fd;
void * mmap_ptr;
int verbose = 0;
int isRead = 1;
int isWrite = 1;
off_t mask_addr;

// variables to store the mapped address of the interesting registers
void * mapped_PIOC_OER_addr;
void * mapped_PIOC_ODR_addr;
void * mapped_PIOC_SODR_addr;
void * mapped_PIOC_CODR_addr;
void * mapped_PIOC_ODSR_addr;
void * mapped_PIOC_PDSR_addr;

init_memoryToIO(void) {
	// to map in a local page the peripheral address registers used 
    mem_fd = -1;

    if ((mem_fd = open(DEV_MEM, O_RDWR | O_SYNC)) < 0) {
        printf("open of " DEV_MEM " failed");
        return 1;
    } else 
        if (verbose) printf("open(" DEV_MEM "O_RDWR | O_SYNC) okay\n");

	mask_addr = (PIOC_OER & ~MAP_MASK);  // preparation of mask_addr (base of the memory accessed)

    if (verbose) printf ("Mask address = %08x\n",mask_addr);
	
	mmap_ptr = (void *)-1;
    mmap_ptr = mmap(0, MAP_SIZE, PROT_READ | PROT_WRITE,
                       MAP_SHARED, mem_fd, mask_addr);
    if (verbose) printf ("Mmap_ptr = %08x\n",mmap_ptr);

					   
    if ((void *)-1 == mmap_ptr) {
        printf("addr=0x%x, mask_addr=0x%lx :\n", PIOC_OER,
                mask_addr);
        printf("    mmap");
        return 1; 
    } 
    if (verbose) printf("mmap() ok, mask_addr=0x%lx, mmap_ptr=%p\n", mask_addr, mmap_ptr);
	mapped_PIOC_OER_addr = mmap_ptr + (PIOC_OER & MAP_MASK);
	mapped_PIOC_ODR_addr = mmap_ptr + (PIOC_ODR & MAP_MASK);
	mapped_PIOC_SODR_addr = mmap_ptr + (PIOC_SODR & MAP_MASK);
	mapped_PIOC_CODR_addr = mmap_ptr + (PIOC_CODR & MAP_MASK);
	mapped_PIOC_ODSR_addr = mmap_ptr + (PIOC_ODSR & MAP_MASK);
	mapped_PIOC_PDSR_addr = mmap_ptr + (PIOC_PDSR & MAP_MASK);
	return 0;
}

close_memoryToIO(void) {
	// closing memory mapping
	if (-1 == munmap(mmap_ptr, MAP_SIZE)) {
        printf("mmap_ptr=%p:\n", mmap_ptr);
        printf("    munmap");
        return 1;
    } else if (verbose) printf("call of munmap() ok, mmap_ptr=%p\n", mmap_ptr);
    if (mem_fd >= 0)
        close(mem_fd);
    return 0;
}

unsigned int setPortCinInput(void) {
	// put PortC in input mode
    *((unsigned long *)mapped_PIOC_ODR_addr) = 0xffffffff;

	return 0;
}

unsigned int setPortCinOutput(void) {
	// put PortC in output mode
    *((unsigned long *)mapped_PIOC_OER_addr) = 0xffffffff;

	return 0;
}

unsigned int readGeneralRegister(unsigned int reg) {
	// returns the content of the CPU register reg
	void * ap;
    unsigned long ul;

    ap = mmap_ptr + (reg & MAP_MASK);
	// read the register
	ul = *((unsigned long *)ap);
	if (verbose) printf("read: addr=0x%x, val=0x%x\n", reg, (unsigned int)ul);

	return (unsigned int)ul;
}

unsigned int readPortCoutbits(void) {
	// returns the content of the register reg
    unsigned long ul;

	// read the register
	ul = *((unsigned long *)mapped_PIOC_ODSR_addr);
	if (verbose) printf("read: addr=0x%x, val=0x%x\n", PIOC_ODSR, (unsigned int)ul);

	return (unsigned int)ul;
}

unsigned int readPortCinbits(void) {
	// returns the content of the register reg
    unsigned long ul;

	// read the register
	ul = *((unsigned long *)mapped_PIOC_PDSR_addr);
	if (verbose) printf("read: addr=0x%x, val=0x%x\n", PIOC_PDSR, (unsigned int)ul);

	return (unsigned int)ul;
}

void writePortC(unsigned int data) {
	// write the output registers of Port C with the value "data"
	
    *((unsigned long *)mapped_PIOC_SODR_addr) = data;
    *((unsigned long *)mapped_PIOC_CODR_addr) = ~data;
}

unsigned int setPortCbit3inOutput(void) {
	// put PortC in output mode
    *((unsigned long *)mapped_PIOC_OER_addr) = 0x00000008;

	return 0;
}

void fastDoublePulsePortC3(void) {
	// write a fast double updown pulse on PortC bit 3
	
    *((unsigned long *)mapped_PIOC_SODR_addr) = 0x00000008;
    *((unsigned long *)mapped_PIOC_CODR_addr) = 0x00000008;
    *((unsigned long *)mapped_PIOC_SODR_addr) = 0x00000008;
    *((unsigned long *)mapped_PIOC_CODR_addr) = 0x00000008;
}


	
int main(int argc, char * argv[])
{
	unsigned int i, inbits, outbits;
	
	printf("FastIO_C example program for AriaG25\n");
	
	if (init_memoryToIO()) {
		printf ("Error in init_memoryToIO() \n");
		return 1;
	}		
	
	setPortCbit3inOutput();
	
	for (i=0; i< 1000000; i++) {
		fastDoublePulsePortC3();
	}

	inbits = readPortCinbits();
	printf("PortC reading inbits:  %08x\n",inbits);
	outbits = readPortCoutbits();
	printf("PortC reading outbits: %08x\n",outbits);
	
	if (close_memoryToIO()) {
		printf ("Error in close_memoryToIO() \n");
		return 1;
	}		
 		
}
