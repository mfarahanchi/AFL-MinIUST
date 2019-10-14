#include <stdio.h>
#include <stdlib.h>

void tabriz() {
    printf("Hello from Tabriz!\n");
}

void tehran() {
    printf("Hello from Tehran!\n");
}

int main(int argc, char** argv)
{
    char *cc=argv[1];
    int c = atoi(cc);

    if(c==1) {
        tabriz();
        tehran();
    } else if(c==2) {
        tehran();
        tabriz();
    }
    return 0;
}