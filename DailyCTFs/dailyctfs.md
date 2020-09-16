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
- Steg 1
- amy
- SHA256ed
- Discord Flag
- Keywords Ugh!
- Random XOR


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
