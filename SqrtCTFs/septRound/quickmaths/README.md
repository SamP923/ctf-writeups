## Quick Maths
> My teacher sent me some massive homework!
> Can you solve it for me?

When connecting, we're given a string that looks something like 
```
72857789302222-95357471421734
25254833624719+80134199293517
```

This goes on for 300 lines. To automate the netcat connection, we can use the pwntools python module. 

```
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
```

Flag: `flag{w0w_qu1ck_m4th5}`