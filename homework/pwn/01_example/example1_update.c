#include <stdio.h>

#define ROOTPASSWD "AAANB"

char passwd[16];

int main(int argc, char *argv[])
{
    char buffer[32];
    int rootuser = 0;

    scanf("%s", passwd);
    getchar();
    if (!strcmp(passwd, ROOTPASSWD))
    {
        rootuser = 1;
    }

    fgets(buffer, 48, stdin);

    if (rootuser)
    {
        printf("you are the root...");
        /* privilege code */
    }
    else
    {
        printf("you are normal user...");
        /* inprivilege code */
    }
    exit(0);
}
