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