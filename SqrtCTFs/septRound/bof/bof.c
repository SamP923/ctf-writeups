#include <stdio.h>
#include <string.h>

int main(void)
{
  long code = 0;
  char name[64];
  
  setbuf(stdout, NULL);
  setbuf(stdin, NULL);
  setbuf(stderr, NULL);

  puts("\n\n\n\nMinecraftcito\nWhere you need to survive all day and all night\nCraft a diamond sword so you can fight\nPlace a torch in a cave to produce some light\nMinecraftcito\n");
  puts("What song do you want me to sing next?\n");
  
  gets(name);
  printf("Sorry, I don't know how to sing that...\n");
  if(code != 0) {
    system("cat flag.txt");
     printf("\n\n\n");
  }
}

