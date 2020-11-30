## Just Add
> Adding all the numbers in this .txt file SHOULD be easy... At least I think so... (Flag format is ictf{The sum of the numbers here})

Yes, yes it is.

```
f = open('sum.txt', 'r')

lines = f.readlines()

sum = 0

for line in lines:
    sum+=int(line)

print("sum: ", sum)
```

Run the script.
```
$ python justadd.py
sum: 74321685214
```

Flag: `ictf{74321685214}`