## The Oracle
> Evil twin was furious due to the last failure. This time he claimed that we need to peek into the future. Try getting the flag. Hint: They forgot to git merge?  
Attachments: https://github.com/ainzs-evil-twin/the-oracle/blob/main/main.py

Given the hint, we check for other branches on the repository and see the redacted xored list. 

Original Script:
```
#!/usr/bin/python3

from codecs import decode
from hashlib import md5
from this import s as zen

def xored_list(str1, str2):
	return [ord(a) ^ ord(b) for a,b in zip(str1, str2)]

flag = input("Paste flag here to get success message: ")

zen = zen.split()

# Since you outsmarted me in `see-the-past` no commit history this time
index_str = <redacted>
assert md5(index_str.encode()).hexdigest() == '4bd23eb13dd04f80b0459b5f2de6c8e7'

x, y, z = index_str[0:2], index_str[2:4], index_str[4:6]
key = zen[int(x)] + '_' + zen[int(y)] + '_' + zen[int(z)]
key = decode(key, 'rot_13')

xored = xored_list(flag, key)

if xored == [7, 12, 0, 57, 15, 24, 19, 71, 60, 83, 8, 3, 65, 24, 88, 83, 15, 43, 2, 3, 83]:
	print('\n\nSuccess :)')
else:
	print('\n\nFailure :(')

```


Solve Script:  
Can find the plaintext of MD5 hash by bruteforcing. Turn the list checked in the final if-statement into a string, then XOR it with the key to get the flag.

```
#!/usr/bin/python3

from codecs import decode
from this import s as zen

def xored_list(str1, str2):
	return [ord(a) ^ ord(b) for a,b in zip(str1, str2)]

flag = ""
xor_list = [7, 12, 0, 57, 15, 24, 19, 71, 60, 83, 8, 3, 65, 24, 88, 83, 15, 43, 2, 3, 83]
for i in xor_list:
  flag += chr(i)

zen = zen.split()

index_str = "878426"

x, y, z = index_str[0:2], index_str[2:4], index_str[4:6]
key = zen[int(x)] + '_' + zen[int(y)] + '_' + zen[int(z)]
key = decode(key, 'rot_13')

xored = xored_list(flag, key)

for i in xored:
  print(chr(i), end="")
```

