<<<<<<< HEAD
# [√-1 + 1] CTF server September 2020 Round
- Sanity Check
- Robots
- [NOT SOLVED] LONGGGGG CRYPTOOOOO (not available) - 250
- [NOT SOLVED] Linux Skillz (not available) - 50
- [NOT SOLVED] bof (not available) - 50
- [NOT SOLVED] LazyDB - 200
- Hexcelent Moves
- MD5ed
- Biblio
- Hashed Potatoes
- [NOT SOLVED] Quick Maths - 100
- zhiepx
- Infinity Library
=======
# [√-1 + 1] CTF server problems 
September 2020 Round
- Sanity Check
- Robots
- [NOT SOLVED] LONGGGGG CRYPTOOOOO (not available)
- [NOT SOLVED] Linux Skillz (not available)
- [NOT SOLVED] bof (not available)
- [NOT SOLVED] LazyDB (web)
- Hexcelent Moves
- MD5ed
- [NOT SOLVED] Biblio (OSINT)
- Hashed Potatoes
- [NOT SOLVED] Quick Maths (programming/pwntools)
- zhiepx
- [NOT SOLVED] Infinity Library (OSINT)
>>>>>>> d3286bc6cd99e1ef3e6f5b578fdac834d84ea22c
- Steg 1
- amy
- SHA256ed
- Discord Flag
- Keywords Ugh!
- Random XOR
<<<<<<< HEAD
- e
- My Website!
=======
>>>>>>> d3286bc6cd99e1ef3e6f5b578fdac834d84ea22c


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

<<<<<<< HEAD
## Infinity Library
> I lost my flag in an infinite library... Can you find it for me? I think I might have left it in wall 4, in shelf 5, in volume 11... 
> Hint: I think I left the flag on page 353...

Using the address given in babel.txt, we access wall 4, shelf 5, volume 11, page 353 on <https://libraryofbabel.info/>, which gives us this text

> the flag is flag.library,of,babel. replace the periods with curly brackets and r
eplace the commas with underscores.  

Flag: `flag{library_of_babel}                                           
                                     

=======
>>>>>>> d3286bc6cd99e1ef3e6f5b578fdac834d84ea22c
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
<<<<<<< HEAD


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
=======
>>>>>>> d3286bc6cd99e1ef3e6f5b578fdac834d84ea22c
