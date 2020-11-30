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
