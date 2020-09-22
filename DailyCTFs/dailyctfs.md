# [√-1 + 1] CTF server problems 
September 2020 Round
- Sanity Check
- Robots
- [NOT SOLVED] LONGGGGG CRYPTOOOOO (not available) (extra)
- [NOT SOLVED] Linux Skillz (not available)
- [NOT SOLVED] bof (not available)
- [NOT SOLVED] LazyDB
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
- 1337 secret challenge

## Lazy DB



## Hashed Potatoes
> I hashed my password with MD5 100 times! It's so secure, I only needed to make my password 1 character long. The flag is flag{<the password you get>}
> 10502fa81a010bfab50c6cad9745b7d8

Scripting!

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

Reversing!

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

We're heavily hinted that the flag is a number. Numbers in binary are only 6 bits long, so we can either pad the front with two zeros or just take substrings in intervals of 6. 

Flag: `flag{293379041573118045942178062455891115683939605429063126250374632854}`  

## Hello World!
> I​​​​‏​‍​​​​‏‌‎​​​​‎‏‍​​​​‏​‎​​​​‏‏‎​​​​‏‎​​​​​‏‎‍​​​​‏‍‍​​​​‏​‌​​​​‏‍‏​​​​‎‏​​​​​‏‎​​​​​‍​‌​​​​‎‏‏​​​​‏‍‏​​​​‏​‌​​​​‏‎‌​​​​‎‏​​​​​‏​‍​​​​‏‌‎​​​​‍​‍​​​​‏​‎​​​​‎‏​​​​​‏‎​​​​​‏‎‍​​​​‎‏‎​​​​‏‌‏​​​​‌‏‏​​​​‏‎‌​​​​‎‏​​​​​‏‎‌​​​​‏​‏​​​​‌‏‏​​​​‏‎​​​​​‎‏​​​​​‏​‍​​​​‌‏‎​​​​‏‍‏​​​​‎‏​​​​​‎‏‍​​​​‎‏​​​​​‏‎​​​​​‍​‌​​​​‎‏‏​​​​‏‍‏​​​​‍​‌​​​​‏‎‌​​​​‎‏​​​​​‍​‌​​​​‏‏​​​​​‏‎‌​​​​‏‍‏​​​​‍​‍​​​​‎‏​​​​​‎‏‏​​​​‏​‏​​​​‍​‍​​​​‏‌‎​​​​‏‌‎​​​​‍​‌​​​​‏‍​​​​​‏​‎​​​​‍​‌​​​‌​​​ forgot how to program, so I'll just type "Hello World". Much easier than making a program type it for me.

If we take a look at the file in a hex editor, there's a ton of characters between "H" and "ello World". We can see a repeating pattern of E2 80 8x, x being BCDEF. In unicode, we can see that these actual map to spaces -- more specifically, (zero-width spaces)[https://www.utf8-chartable.de/unicode-utf8-table.pl?start=8192&number=128]. We can use an online decoder like [zwsp-steg](https://github.com/offdev/zwsp-steg-js) to get our flag.

Credit to MatthewN for the tip.

Flag: `flag{00pS_1_th0ught_th1s_w4s_4as1er}`

Taking the challenge text, we try that too for the 1337 secret challenge. 

Flag: `flag{super_s3cret_fl4g_subm1t_th1s_f0r_a_s3cr3t_3xtr4_ch4ll3ng3}`