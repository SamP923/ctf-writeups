## SUPER SECURE ENCRYPTER
> I just made a SUPER SECURE ENCRYPTER. It takes your text and encrypts it BEYOND recovery. At least I think so...
> zCR\{fzR*RzkRf>RzkRkfzkRRkzkRk>zkzW*kfWCz}

The encryption algorithm is hard to decrypt because multiple plaintext letters can be mapped to the ciphertext letter. We use the encryption algorithm to make a dictionary. We're given the hint that the flag is all uppercase, so our possible characters are
> {ABCDEFGHIJKLMNOPQRSTUVWXYZ}
Testing numbers gives us an out-of-bounds error, so we know we're not looking at leet text. We print our dictionary for a visual.

```
{:{
f:DISX
z:EJTY
R:CHRW
*:FU
k:AP
>:GV
W:O
C:N
}:}
```

After trying to come up with potential words, I realized that we probably should have delimiters to separate the words. CTF flags usually use underscores, so we add that to our alphabet. One mapping changes from 
`k:AP to k:AP_`

Looking at the mapping (see below), we can guess that most of the `k`'s are going to map to underscores, since flags are usually multiple words. It's then a matter of looking for patterns and testing combinations. 

The first combinations I saw were `WAIT` `ARRAY` and `DONE`. The `WAIT` and `DONE` combinations got me thinking, becuase this particular problem writer has done a flag with similar wording...
> FLAG{THIS_IS_IMPOSSIBLE_RIGHT_WAIT_WHAT_ARE_YOU_DOING...}

Another person had tipped me off that the first word was `SECURE`. Knowing that there was a delimiter was key, because without it, you could get something like `SECUREPRIV` and get stuck. Filling these is, we can guess the rest of our flag

```
{:{
f:DISX		S
z:EJTY		E
R:CHRW		C
*:FU		U
R:CHRW		R
z:EJTY		E

k:AP_		

R:CHRW		R
f:DISX		I
>:GV		G
R:CHRW		H
z:EJTY		T

k:AP_		
				
R:CHRW		W
k:AP_		A
f:DISX		I
z:EJTY		T

k:AP_		

R:CHRW		W
R:CHRW		H
k:AP_		A
z:EJTY		T

k:AP_		_
R:CHRW		H
k:AP_		A
>:GV		V
z:EJTY		E
k:AP_		_
z:EJTY		Y
W:O		O
*:FU		U

k:AP_		_

f:DISX		D
W:O		O
C:N		N
z:EJTY		E
}:}
```

Flag: `flag{SECURE_RIGHT_WAIT_WHAT_HAVE_YOU_DONE}`