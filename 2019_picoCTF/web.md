# Web Exploitation
5/?
- Insp3ct0r, 50 Points
- dont-use-client-side, 100 Points
- logon, 100 Points
- where are the robots, 100 Points
- Client-side-again, 200 Points

## where are the robots
> Can you find the robots? https://2019shell1.picoctf.com/problem/49824/ (link) or http://2019shell1.picoctf.com:49824

This problem references the robots.txt file for websites, which tells search engine crawlers which pages or files can or cannot be requested from the site. Adding robots.txt to the end gives us a page with this:
> User-agent: *
Disallow: /0194a.html

Flag: `picoCTF{ca1cu1at1ng_Mach1n3s_0194a}`


## Client-side-again

Checking the source code, we can see an array _0x5a46 that seems to hold the flag. 
```
var _0x5a46 = ['55670}', '_again_0', 'this', 'Password\x20Verified', 'Incorrect\x20password', 'getElementById', 'value', 'substring', 'picoCTF{', 'not_this'];
```
Typing `_0x5a46` in the console prints the array after it's been righted and gives us the flag.
```
["getElementById", "value", "substring", "picoCTF{", "not_this", "55670}", "_again_0", "this", "Password Verified", "Incorrect password"]
```
Flag: `picoCTF{not_this_again_055670}`


## Open-to-admins

## picobrowser

## Java Script Kiddie

