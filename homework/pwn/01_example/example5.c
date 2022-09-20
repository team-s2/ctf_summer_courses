#include <stdio.h>

int main(int argc, char *argv[])
{
    char buffer[32];
    printf("buffer address: 0x%lx", (long)buffer);
    scanf("%s", buffer);
    return 0;
}