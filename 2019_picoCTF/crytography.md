# Cryptography
- The Numbers, 50 points
- 13, 100 points
- Easy1, 100 Points
- caesar, 100 Points
- Flags, 200 Points
- Mr-Worldwide, 200 Points
- Tapping, 200 Points
- la cifra de, 200 Points
- waves over lambda, 300 Points

## The Numbers
### Description
> The numbers... what do they mean?

### Solution: 
Image given. Convert numbers to letters based on ABC --> 123.  
Flag: `PICOCTF{THENUMBERSMASON}`.  

## 13
### Description
> Cryptography can be easy, do you know what ROT13 is? cvpbPGS{abg_gbb_onq_bs_n_ceboyrz}

### Solution: 
As the name suggests, rotate the given flag by 13 characters.  
Flag: `picoCTF{not_too_bad_of_a_problem}`.  


## Easy1
### Description
> The one time pad can be cryptographically secure, but not when you know the key. Can you solve this? We've given you the encrypted flag, key, and a table to help UFJKXQZQUNB with the key of SOLVECRYPTO. Can you use this table to solve it?

### Solution: 
Table clued in to it being a Vignere cipher, used DCODE.  
Flag is `picoCTF{CRYPTOISFUN}`.  


## caesar
### Description
> Decrypt this message.
Download the file and you're given this:  
```
picoCTF{zolppfkdqeboryfzlktjxksyyl}
```

### Solution:
Name suggests caesar cipher, all 26 cases can be bruteforced to get the flag.  
Flag is `picoCTF{crossingtherubiconwmanvbbo}`.


## Flags
### Description
> What do the flags mean?

### Solution: 
Googling "flag decode" brings you to a [Maritime Signals Code decoder](https://www.dcode.fr/maritime-signals-code). Transcribe flags from the image to get the flag.  
Flag is `PICOCTF{F1AG5AND5TUFF}`.


## Mr-Worldwide
### Description
> A musician left us a message. What's it mean?
```
picoCTF{(35.028309, 135.753082)(46.469391, 30.740883)(39.758949, -84.191605)(41.015137, 28.979530)(24.466667, 54.366669)(3.140853, 101.693207)_(9.005401, 38.763611)(-3.989038, -79.203560)(52.377956, 4.897070)(41.085651, -73.858467)(57.790001, -152.407227)(31.205753, 29.924526)}
```

### Solution: 
Flag: `picoCTF{}`.


## Tapping
### Description
> Theres tapping coming in from the wires. What's it saying nc 2019shell1.picoctf.com 21897.

### Solution: 
Dots and dashes signal morse code. Decode to get the flag.
Flag: `picoCTF{}`.


## la cifra de
### Description
> I  found this cipher in an old book. Can you figure out what it says? Connect with nc 2019shell1.picoctf.com 60147.

### Solution: 
Flag: `picoCTF{}`.


## waves over lambda
### Description
> We made alot of substitutions to encrypt this. Can you decrypt it? Connect with nc 2019shell1.picoctf.com 32282.

### Solution: 
Flag: `picoCTF{}`.
