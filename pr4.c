#include <stdio.h>
#include <stdlib.h>
 
int main(int argc, char** argv)
{
  int c;
  char *nc=argv[0];
  int n = atoi(nc);
 
  printf("How many times you want to display it?\n");
//   scanf("%d", &n);
 
  for (c=1; c<=n; c++)
     printf("Hello world!\n");
 
  return 0;
}