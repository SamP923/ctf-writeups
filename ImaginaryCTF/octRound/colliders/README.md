## Colliders are the best Unity Components!
> Hey! Can you bypass my login system?

```
from hashlib import md5

hp = input("Enter plaintext: ")

p = bytes.fromhex(hp)

h = md5(p).hexdigest()

if h[6:-6] == "25255fb1a26e4bc422ae" and hp != "d131dd02c5e6eec4693d9a0698aff95c2fcab58712467eab4004583eb8fb7f8955ad340609f4b30283e488832571415a085125e8f7cdc99fd91dbdf280373c5bd8823e3156348f5bae6dacd436c919c6dd53e2b487da03fd02396306d248cda0e99f33420f577ee8ce54b67080a80d1ec69821bcb6a8839396f9652b6ff72a70":
    print("Correct! Submit ictf{your_input_here}")
else:
    print("Wrong!")
```

This script checks on the that the middle 12 characters of the calcualted MD5 hash are equal, but not from the given hash. This results in something called MD5 collisions (found by Googling "md5 hashes that have the same middle as another string). This specific problem actually uses a famous pair, as shown on this website. We wrap the second hash in the flag format to get our flag.

Flag: `ictf{d131dd02c5e6eec4693d9a0698aff95c2fcab50712467eab4004583eb8fb7f8955ad340609f4b30283e4888325f1415a085125e8f7cdc99fd91dbd7280373c5bd8823e3156348f5bae6dacd436c919c6dd53e23487da03fd02396306d248cda0e99f33420f577ee8ce54b67080280d1ec69821bcb6a8839396f965ab6ff72a70}`