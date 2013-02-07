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

// SPI registers

#define SPI_BASE 		0xf0000000
#define SPI0_CR    		0x00
#define SPI0_MR    		0x04
#define SPI0_RDR   		0x08
#define SPI0_TDR   		0x0C
#define SPI0_SR   		0x10
#define SPI0_IDR  		0x18
#define SPI0_CSR0 		0x30
#define SPI0_CSR1 		0x34
#define SPI0_WPMR  		0xE4
#define SPI0_WPSR  		0xE8


// PIOC registers

#define PIO_BASE 		0xFFFFF400 
#define PIO_PDR			0x04
#define PIO_PUER		0x64

int memspi_fd;
int mempio_fd;

void * mmap_ptr;
void * mmap_ptr_pio;

int verbose = 0;
int isRead = 1;
int isWrite = 1;
off_t mask_addr;

// variables to store the mapped address of the interesting registers
void * mapped_SPI0_CR_addr;
void * mapped_SPI0_MR_addr;
void * mapped_SPI0_RDR_addr;
void * mapped_SPI0_TDR_addr;
void * mapped_SPI0_SR_addr;
void * mapped_SPI0_IDR_addr;
void * mapped_SPI0_CSR0_addr;
void * mapped_SPI0_CSR1_addr;
void * mapped_SPI0_WPMR_addr;
void * mapped_SPI0_WPSR_addr;

void * mapped_PIO_PDR_addr;
void * mapped_PIO_PUER_addr;


init_memoryToIO(void) {
	// to map in a local page the peripheral address registers used 
    memspi_fd = -1;
    mempio_fd = -1;

	// Shared map for SPI registers
    if ((memspi_fd = open(DEV_MEM, O_RDWR | O_SYNC)) < 0) {
        printf("open of " DEV_MEM " failed");
        return 1;
    }
	mask_addr = (SPI_BASE & ~MAP_MASK);  // preparation of mask_addr (base of the memory accessed)
	mmap_ptr = (void *)-1;
    mmap_ptr = mmap(0, MAP_SIZE, PROT_READ | PROT_WRITE,MAP_SHARED, memspi_fd, mask_addr);
					   
    if ((void *)-1 == mmap_ptr) {
        printf("addr=0x%x, mask_addr=0x%lx :\n", SPI_BASE,mask_addr);
        return 1; 
    } 

	mapped_SPI0_CR_addr   = mmap_ptr + ((SPI_BASE+SPI0_CR)   & MAP_MASK);
	mapped_SPI0_MR_addr   = mmap_ptr + ((SPI_BASE+SPI0_MR)   & MAP_MASK);
	mapped_SPI0_RDR_addr  = mmap_ptr + ((SPI_BASE+SPI0_RDR)  & MAP_MASK);
	mapped_SPI0_TDR_addr  = mmap_ptr + ((SPI_BASE+SPI0_TDR)  & MAP_MASK);
	mapped_SPI0_SR_addr   = mmap_ptr + ((SPI_BASE+SPI0_SR)   & MAP_MASK);
	mapped_SPI0_IDR_addr  = mmap_ptr + ((SPI_BASE+SPI0_IDR)  & MAP_MASK);
	mapped_SPI0_CSR0_addr = mmap_ptr + ((SPI_BASE+SPI0_CSR0) & MAP_MASK);
	mapped_SPI0_CSR1_addr = mmap_ptr + ((SPI_BASE+SPI0_CSR1) & MAP_MASK);
	mapped_SPI0_WPMR_addr = mmap_ptr + ((SPI_BASE+SPI0_WPMR) & MAP_MASK);
	mapped_SPI0_WPSR_addr = mmap_ptr + ((SPI_BASE+SPI0_WPSR) & MAP_MASK);

	// Shared map for PIO registers
    if ((mempio_fd = open(DEV_MEM, O_RDWR | O_SYNC)) < 0) {
        printf("open of " DEV_MEM " failed");
        return 1;
    }
	mask_addr = (PIO_BASE & ~MAP_MASK);  // preparation of mask_addr (base of the memory accessed)

	mmap_ptr_pio = (void *)-1;
    mmap_ptr_pio = mmap(0, MAP_SIZE, PROT_READ | PROT_WRITE,MAP_SHARED, mempio_fd, mask_addr);
					   
    if ((void *)-1 == mmap_ptr_pio) {
        printf("addr=0x%x, mask_addr=0x%lx :\n", PIO_BASE,mask_addr);
        return 1; 
    } 

	mapped_PIO_PDR_addr   = mmap_ptr_pio + ((PIO_BASE+PIO_PDR)   & MAP_MASK);
	mapped_PIO_PUER_addr   = mmap_ptr_pio + ((PIO_BASE+PIO_PUER)   & MAP_MASK);

	return 0;
}

close_memoryToIO(void) {
	// Close the shared map for SPI register
	if (-1 == munmap(mmap_ptr, MAP_SIZE)) {
        printf("mmap_ptr=%p:\n", mmap_ptr);
        return 1;
    }
    if (memspi_fd >= 0)
        close(memspi_fd);

	// Close the shared map for PIO register
	if (-1 == munmap(mmap_ptr_pio, MAP_SIZE)) {
        printf("mmap_ptr_pio=%p:\n", mmap_ptr_pio);
        return 1;
    } else
    if (mempio_fd >= 0)
        close(mempio_fd);
    return 0;
}

void mydelay(void) {
	unsigned long ul;
	int a;
	int c=0;
	for(a=0;a<8000;a++) {
		ul = *((unsigned long *)mapped_SPI0_SR_addr);
		if (ul&(1<<9)) return;
		c++;
	}
}

int main(int argc, char * argv[])
{
	unsigned int i, inbits, outbits;
	unsigned int value;
	int c;
	unsigned long ul;
	int ch;
	int dac_value;


	printf("SPI test on AriaG25\n");

	if (init_memoryToIO()) {
		printf ("Error in init_memoryToIO() \n");
		return 1;
	}		

	// PIO initialization
	// Disable GPIO on PA7,11,12,13,14
	*((unsigned long *)mapped_PIO_PDR_addr) = 0x7880;
	// Enable the internal pull-up on PA7,11,12,13,14
	*((unsigned long *)mapped_PIO_PUER_addr) = 0x7880;

	// Enable SPI
	*((unsigned long *)mapped_SPI0_CR_addr) = 0x00000001;

	// Disable all interrupts
	*((unsigned long *)mapped_SPI0_IDR_addr) = 0x0000030F;

	// Master mode
	*((unsigned long *)mapped_SPI0_MR_addr) = 0x00000013;

	// Definizione modalita SPI per ADC su CS0 (16bit)
	*((unsigned long *)mapped_SPI0_CSR0_addr) = 0x00FF2981;
	// Definizione modalita SPI per DAC su CS1 (16bit)
	*((unsigned long *)mapped_SPI0_CSR1_addr) = 0x00FF2981;

	for (;;) { 
		// Sezione ADC

		for (ch=0;ch<8;ch++) { 
			// Write a data
			*((unsigned long *)mapped_SPI0_TDR_addr) = (ch<<11);
			mydelay();
			*((unsigned long *)mapped_SPI0_TDR_addr) = (ch<<11);
			mydelay();
			*((unsigned long *)mapped_SPI0_TDR_addr) = (ch<<11);
			mydelay();

			ul = *((unsigned long *)mapped_SPI0_RDR_addr);
			mydelay();

			printf("%04d ",((unsigned int)ul)&0x00000FFF);
		}
		printf("\n");

		
		// Sezione DAC con AD5317
		// Genera un'onda triangolare
		for (ch=0;ch<4;ch++) { 
			// Se AD5317
			for (dac_value=0;dac_value<1024;dac_value++) { 
				*((unsigned long *)mapped_SPI0_TDR_addr) = (1<<16)|(ch<<14)|(dac_value<<2);
				mydelay();
			}
			for (dac_value=1023;dac_value>=0;dac_value--) { 
				*((unsigned long *)mapped_SPI0_TDR_addr) = (1<<16)|(ch<<14)|(dac_value<<2);
				mydelay();
			}
		}

		// Sezione DAC con AD5307
		// Genera un'onda triangolare
/*		for (ch=0;ch<4;ch++) { 
			// Se AD5307
			for (dac_value=0;dac_value<256;dac_value++) { 
				*((unsigned long *)mapped_SPI0_TDR_addr) = (1<<16)|(ch<<14)|(dac_value);
				mydelay();
			}
			for (dac_value=255;dac_value>=0;dac_value--) { 
				*((unsigned long *)mapped_SPI0_TDR_addr) = (1<<16)|(ch<<14)|(dac_value);
				mydelay();
			}
		}
*/

	}

	if (close_memoryToIO()) {
		printf ("Error in close_memoryToIO() \n");
		return 1;
	}		
}
