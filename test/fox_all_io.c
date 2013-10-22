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

// PIO port base address
#define PIO_BASE 		0xFFFFF400 
#define PIOA_BASE 		0xFFFFF400 
#define PIOB_BASE 		0xFFFFF600 
#define PIOC_BASE 		0xFFFFF800 

// PIO registers
#define PIO_PER			0x0000
#define PIO_PDR			0x0004
#define PIO_PUER		0x0064

int mempio_fd;

void * mmap_ptr;
void * mmap_ptr_pio;

int verbose = 0;
int isRead = 1;
int isWrite = 1;
off_t mask_addr;

void * mapped_PIOA_PER_addr;
void * mapped_PIOA_PDR_addr;
void * mapped_PIOA_PUER_addr;

void * mapped_PIOB_PER_addr;
void * mapped_PIOB_PDR_addr;
void * mapped_PIOB_PUER_addr;

void * mapped_PIOC_PER_addr;
void * mapped_PIOC_PDR_addr;
void * mapped_PIOC_PUER_addr;


init_memoryToIO(void) {
	// to map in a local page the peripheral address registers used 
    mempio_fd = -1;

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

	mapped_PIOA_PER_addr   = mmap_ptr_pio + ((PIOA_BASE+PIO_PER)   & MAP_MASK);
	mapped_PIOA_PDR_addr   = mmap_ptr_pio + ((PIOA_BASE+PIO_PDR)   & MAP_MASK);
	mapped_PIOA_PUER_addr  = mmap_ptr_pio + ((PIOA_BASE+PIO_PUER)  & MAP_MASK);

	mapped_PIOB_PER_addr   = mmap_ptr_pio + ((PIOB_BASE+PIO_PER)   & MAP_MASK);
	mapped_PIOB_PDR_addr   = mmap_ptr_pio + ((PIOB_BASE+PIO_PDR)   & MAP_MASK);
	mapped_PIOB_PUER_addr  = mmap_ptr_pio + ((PIOB_BASE+PIO_PUER)  & MAP_MASK);

	mapped_PIOC_PER_addr   = mmap_ptr_pio + ((PIOC_BASE+PIO_PER)   & MAP_MASK);
	mapped_PIOC_PDR_addr   = mmap_ptr_pio + ((PIOC_BASE+PIO_PDR)   & MAP_MASK);
	mapped_PIOC_PUER_addr  = mmap_ptr_pio + ((PIOC_BASE+PIO_PUER)  & MAP_MASK);

	return 0;
}

close_memoryToIO(void) {
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
	int a;
	int c=0;
	for(a=0;a<8000;a++) {
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


	printf("Set all GPIO\n");

	if (init_memoryToIO()) {
		printf ("Error in init_memoryToIO() \n");
		return 1;
	}		

	// PIO initialization
	// Disable GPIO 
	*((unsigned long *)mapped_PIOA_PER_addr) = 0x0000;
	*((unsigned long *)mapped_PIOB_PER_addr) = 0x000F;
	*((unsigned long *)mapped_PIOC_PER_addr) = 0x0038;

	// Enable the internal pull-up on PA7,11,12,13,14
	//*((unsigned long *)mapped_PIO_PUER_addr) = 0x7880;

	if (close_memoryToIO()) {
		printf ("Error in close_memoryToIO() \n");
		return 1;
	}		
}
