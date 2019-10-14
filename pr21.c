#include <stdio.h>
#include <stdlib.h>

int main(int argc, char** argv)
{
    char *cc=argv[1];
    int c = atoi(cc);

    if (c>0) {
        printf("\n c>0");
    } else {
        printf("\n c<=0");
    }
    
    return 0;
}