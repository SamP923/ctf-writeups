from pwn import *

stillInp = True
conn = remote('netcat.et3rnos.ga', 10000)

while stillInp:
	line = conn.readline()
	print(line)
	if (b'+' in line):
		a = int(line.split(b'+')[0]) + int(line.split(b'+')[1])
		print(a)
		conn.sendline(str(a))
	elif (b'-' in line):
		a = int(line.split(b'-')[0]) - int(line.split(b'-')[1])
		print(a)
		conn.sendline(str(a))
	else:
		stillInp = False