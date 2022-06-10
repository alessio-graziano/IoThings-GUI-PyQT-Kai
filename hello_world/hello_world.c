#include <stdio.h>
#include <unistd.h>

int main(int argc, char *argv[])
{
    unsigned int i=0;
    while (1) {
        printf("%d: Hello World!\n", i+=1);
        sleep(1);
    }
    return 0;
}