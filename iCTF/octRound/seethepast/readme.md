## See The Past
> Ainz's evil twin has returned and is giving out unreasonable challenges to solve for the flag. We managed to track down the source of a challenge on evil twin's GitHub repo. Can you help recover the flag? The issue is that you might need to take a look into the past.
Attachments: https://github.com/ainzs-evil-twin/see-the-past/blob/master/main.py


If we check the repository, we're given a caesar cipher and xor script to reverse with the key redacted. If we check the commit history, and we can find the redacted key.


Original script:
```
#!/usr/bin/python3

def caesar(plaintext, shift):
	ciphertext = ''
	for i in plaintext:
		if 97 <= ord(i) <= 122:
			ciphertext += chr((ord(i) - 97 + shift)%26 + 97)
		else:
			ciphertext += i
	return ciphertext

def xored_list(str1, str2):
	return [ord(a) ^ ord(b) for a,b in zip(str1, str2)]

plaintext = input("String to be encrypted: ")
key = "dQw4w9WgXcQ"

sixth_shift = caesar(plaintext, 6)
xored = xored_list(sixth_shift, key*3)

if xored == [11, 56, 13, 88, 12, 65, 54, 21, 107, 86, 14, 17, 61, 40, 78, 24, 74, 60, 56, 63, 27, 98, 59, 34, 70, 64, 68, 68]:
	print('Impossible!')
else:
	print('Mwahahaha... You\'ll need to go back in time to get this')
``` 

Solve script:  
XOR the list check in the if-statement with the repeated key. Turn the XORed list into a string, then reverse the rotation.
```
def caesar(plaintext, shift):
	ciphertext = ''
	for i in plaintext:
		if 97 <= ord(i) <= 122:
			ciphertext += chr((ord(i) - 97 + shift)%26 + 97)
		else:
			ciphertext += i
	return ciphertext

def xoring(xlist,keylist):
  return [ord(b) ^ a for a, b in zip(xlist, keylist)]

key = "dQw4w9WgXcQ"

xored = [11, 56, 13, 88, 12, 65, 54, 21, 107, 86, 14, 17, 61, 40, 78, 24, 74, 60, 56, 63, 27, 98, 59, 34, 70, 64, 68, 68]

result = xoring(xored, list(key*3))

flag = ""
for i in result:
  flag += chr(i)

print(caesar(flag, 20))
```