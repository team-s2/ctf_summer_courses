#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(int argc, char *argv[])
{
    int offset;
    int size;
    char buffer[64];
    char *ptr;

    printf("please input: ");
    scanf("%s", buffer);
    printf("you input %d characters\n", strlen(buffer));
    printf("your data: %s\n", buffer);

    printf("index: ");
    scanf("%d", &offset);
    getchar();
    buffer[offset] = getchar();

    printf("size: ");
    scanf("%d", &size);
    if (size >= strlen(buffer))
        printf("size too large");
    else {
        ptr = malloc(strlen(buffer));
        memcpy(ptr, buffer, size);
        free(ptr);
    }

    free(ptr);
    return 0;
}
