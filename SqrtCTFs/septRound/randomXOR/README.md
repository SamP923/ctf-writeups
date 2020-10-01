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