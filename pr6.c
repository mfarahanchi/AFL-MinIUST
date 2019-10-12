#include <stdio.h>
#include <stdlib.h>
 
int main(int argc, char** argv)
{
    int c;
    char *nc=argv[1];
    char *ponpc=argv[2]; //"p"rint or "n"ot to "p"rint? "c"har
    int n = atoi(nc);
    int ponp = atoi(ponpc);

    if(ponp>0)
        for (c=1; c<=n; c++)
            printf("Hello world!\n");
    return 0;
}