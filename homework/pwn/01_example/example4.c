#include <stdio.h>

void bof(char *s)
{
    char buffer[16];
    strcpy(s, buffer);
}

int bridge(char *s)
{
    bof(s);
}

int main(int argc, char *argv[])
{
    char buffer[32];
    scanf("%s", buffer);
    bridge(buffer);
    return 0;
}