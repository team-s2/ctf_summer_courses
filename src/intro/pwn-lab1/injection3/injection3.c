#define _GNU_SOURCE

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdint.h>
#include <stdbool.h>
#include <unistd.h>

#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <sys/mman.h>
#include <errno.h>

#define MAP_ADDR (0x10000)
#define CODE_SIZE (0x100)

void prepare()
{
    setvbuf(stdin, 0LL, 2, 0LL);
    setvbuf(stdout, 0LL, 2, 0LL);
    alarm(60);
}

bool codecheck(char* buf, int size)
{
    // do not allow syscall here
    int i;
    for(i = 0; i < size; i += 2) {
        if (*(uint16_t*)(buf + i) == 0x050f) {
            return false;
        }
    }
    return true;
}

int main(int argc, char const *argv[])
{
    void* address;
    int size = sysconf(_SC_PAGESIZE);
    int a, b, c;
    int (*funcptr)(int, int);
    int error = -1;

    prepare();

    a = random() & 0xff;
    b = random() & 0xff;

    address = mmap(MAP_ADDR, size, PROT_EXEC | PROT_READ | PROT_WRITE, MAP_PRIVATE | MAP_ANONYMOUS | MAP_FIXED, -1, 0);

    if (address == MAP_FAILED) {
        perror("mmap");
        exit(-1);
    }

    funcptr = address;

    printf("Hello there, once you finish the delegate tasks I requested,\nI will give you your flag :)\n");
    printf("*** DO NOT CHEAT ME, BIG MA IS WATHCING YOU ***\n");
    printf("-----------------------------------------------------------\n");

    printf("Request-1: give me code that performing ADD\n");
    read(STDIN_FILENO, address, CODE_SIZE);
    if (!codecheck(address, size)) {
        printf("bad payload, be cool okay?\n");
        goto fail;
    }

    c = funcptr(a, b);

    if (c != a + b) {
        printf("you fail, try again\n");
        goto fail;
    }
    printf("goooooood, next one\n");

    printf("Request-2: give me code that performing SUB\n");
    read(STDIN_FILENO, address, CODE_SIZE);
    if (!codecheck(address, size)) {
        printf("bad payload, be cool okay?\n");
        goto fail;
    }

    c = funcptr(a, b);

    if (c != a - b) {
        printf("you fail, try again\n");
        goto fail;
    }
    printf("goooooood, next one\n");

    printf("Request-3: give me code that performing AND\n");
    read(STDIN_FILENO, address, CODE_SIZE);
    if (!codecheck(address, size)) {
        printf("bad payload, be cool okay?\n");
        goto fail;
    }

    c = funcptr(a, b);

    if (c != (a & b)) {
        printf("you fail, try again\n");
        goto fail;
    }
    printf("goooooood, next one\n");

    printf("Request-4: give me code that performing OR\n");
    read(STDIN_FILENO, address, CODE_SIZE);
    if (!codecheck(address, size)) {
        printf("bad payload, be cool okay?\n");
        goto fail;
    }

    c = funcptr(a, b);

    if (c != (a | b)) {
        printf("you fail, try again\n");
        goto fail;
    }
    printf("goooooood, fianl one\n");

    printf("Request-5: give me code that performing XOR\n");
    read(STDIN_FILENO, address, CODE_SIZE);
    if (!codecheck(address, size)) {
        printf("bad payload, be cool okay?\n");
        goto fail;
    }

    c = funcptr(a, b);

    if (c != (a ^ b)) {
        printf("you fail, try again\n");
        goto fail;
    }
    
    printf("Soooooooo wonderful, here is your flag:\n");
    printf("%s", getenv("FLAG"));
    error = 0;

fail:
    munmap(address, size);
    return error;
}