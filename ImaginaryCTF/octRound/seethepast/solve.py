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