#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <stdint.h>
#include <string.h>
#include <sys/mman.h>

// #define XORKEY (0x41)
#define DEBUG

#ifdef DEBUG
#include <errno.h>
#endif

int main(int, char**);

void packing()
{
    void* start = (void*)main; // main start address

    // align start address to page granularity

    // enable write to text
    if (mprotect(XXX, XXX, PROT_READ|PROT_WRITE|PROT_EXEC) < 0) {
        // fail
    }

    // decrypt main
    // ...
    
    // recover the flag
    if (mprotect(XXX, XXX, PROT_READ|PROT_EXEC) < 0) {
        // fail
    }

    return;
}

class mypack {
public:
    mypack(void) { packing(); }
};

mypack gpacker;

// of course you can write your own program here

char password[] = "VeRY_VERy_h4RD_aNd_S3curE_pA5SWoRD";

int main(int argc, char* argv[])
{
    char input[64] = {0};

    read(STDIN_FILENO, input, 34);

    if (strcmp(password, input)) {
        printf("error\n");
    } else {
        printf("ok\n");
    }

    return 0;
}


