# [√-1 + 1] CTF server problems 
September 2020 Round
- Sanity Check
- Robots
- [NOT SOLVED] LONGGGGG CRYPTOOOOO (not available) (extra)
- Linux Skillz
- bof
- LazyDB
- Hexcelent Moves
- MD5ed
- Biblio
- Hashed Potatoes
- [NOT SOLVED] Quick Maths 
- zhiepx
- Infinity Library
- Steg 1
- amy
- SHA256ed
- Discord Flag
- Keywords Ugh! (extra)
- Random XOR
- e
- My Website!
- SUPER SECURE ENCRYPTER
- Not So Easy Binary Decode
- Whitened
- Hello World!
- 1337 secret challenge (extra)
- WASM
- The online classroom.
- The Flag Is In The Past
- MD5²
- Braille
- Whirlpool

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


## Infinity Library
> I lost my flag in an infinite library... Can you find it for me? I think I might have left it in wall 4, in shelf 5, in volume 11... 
> Hint: I think I left the flag on page 353...

Using the address given in babel.txt, we access wall 4, shelf 5, volume 11, page 353 on <https://libraryofbabel.info/>, which gives us this text

> the flag is flag.library,of,babel. replace the periods with curly brackets and r
eplace the commas with underscores.  

Flag: `flag{library_of_babel}


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
This is RSA! Credit to <https://blog.kuhi.to/picoctf_2019_crypto_writeup> becuase I still don't know how to do it.

```
ciphertext = plaintext ^ e mod n = plaintext ^ e, if plaintext ^ e < n
```
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
> https://digitalmortifiedactivecell.mendel3.repl.co/
> Hints: https://stackoverflow.com/questions/51562325/webassembly-correct-way-to-get-a-string-from-a-parameter-with-memory-address
> https://marcoselvatici.github.io/WASM_tutorial/

This is the jankiest and definitely not intended way to solve, especially given the first hint. The following code checks through all values in WASM memory, sees if they are not 0, checks if the decimal corresponds to a printable ASCII character, then prints it. This is input to the Javacript console.

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