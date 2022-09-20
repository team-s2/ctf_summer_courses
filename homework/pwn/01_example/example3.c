#include <stdio.h>
#include <stdlib.h>

void backdoor()
{
    printf("Hi Backdoor\n");
    system("/bin/sh");
}

void normal()
{
    printf("Hi Normal\n");
    return;
}

int main(int argc, char *argv[])
{
    void (*ptr)(void) = normal;
    char buffer[32];
    gets(buffer);
    puts(buffer);
    ptr();
    return 0;
}
