# [√-1 + 1] CTF server problems 
October 2020 Round

Ranking: 1/60 with 2555 points (30/30 challenges solved).

| Challenge               | Type | Points |
|-------------------------|------|--------|
| Welcome to Round 3! | Misc | 15 |
| Meta | Forensics | 100 |
| [Did you feel that wave?](didyoufeelthatwave/) | Misc | 175 |
| [Save Trees!](savetrees/) | Rev | 80 |
| [Colliders are the best Unity Components!](colliders/) | Rev | 60 |
| Whitened 2.0 | Misc | 100 |
| [AppleBot](#applebot) | Misc | 150 |
| [Blinking Lights](#blinking-lights) | Crypto | 50 |
| [Optimization](optimization/) | Programming | 150 |
| Out of Office... | OSINT | 100 |
| [Is this art?](#is-this-art) | Forensics | 50 | 
| [Fuzzy](#fuzzy) | Forensics | 100 |
| [Just Add](justadd/) | Programming | 50 |
| Flag on discord? | OSINT | 50 |
| Impossible... Right? | Crypto | 50 |
| Wow A Fine Day! | Crypto | 50 |
| Runes | Crypto | 50 |
| Factors | Programming | 100 |
| Encoding | Crypto | 100 |
| More Runes... | Crypto | 75 |
| [seed12](seed12/) | Programming | 150 |
| Base... What? | Crypto | 50 |
| [See The Past](seethepast/) | Rev/OSINT | 100 |
| Emojis | Crypto | 50 |
| [The Oracle](theoracle/) | Rev/OSINT | 100 |
| Calendars | OSINT | 100 |
| Upercase | Crypto | 50 |
| Rails | Crypto | 50 |
| [Flag Checker](flagchecker/) | RE/Crypto | 100 |
| [Colors](#colors) | Forensics | 100 |

My shorter writeups that don't involve a script are on this main doc. Check out individual problems and files in their respective folders.


## Applebot
> I made a new Discord Bot! Its called @AppleBot and it gives you apples! It seems to have a lot of Apples it self though... Try to exploit it to get enough Apples to buy the flag in the shop! Or you could do it manually, but that would take a long time... Have Fun!

We first take a look at the commands we can use with the bot.
```
​No Category:
  Applebot Tells you how many Apples @AppleBot has
  balance  Gets your balance.
  buy      Buys stuff.
  clear    Clears all your Apples
  help     Shows this message
  shop     Displays the shop.
  transfer Transfers apples to someone else.
  work     Gives you apples.

Type $help command for more info on a command.
You can also type $help category for more info on a category.
```

If we check in the shop, there's just one item:
```
100000000000000000000000 Apples: flag
```

Working will give you 6 apples, which would take a very long time. The key command here is the `transfer` command. 
```
$transfer <person> <amount>

Transfers apples to someone else.
```

When we try to transfer apples to ourselves, our Discord tag doesn't actually ping us and the bot doesn't have a response. However, we find that we can transfer apples to the bot. If we test a negative number, we can transfer apples from the bot to ourselves. Hopefully the bot has an infinite amount!

```
$transfer @AppleBot -100000000000000000000000
You sent -100000000000000000000000 apples to AppleBot#xxxx

$balance
You have 100000000000000000000011 apples.

$buy flag
You bought the flag for 100000000000000000000 apples.

ictf{S0_M4NY_APPl3$_7OO_MUCH_W0RK_$0_W3_H4CK}
```

Flag: `ictf{S0_M4NY_APPl3$_7OO_MUCH_W0RK_$0_W3_H4CK}`


## Blinking Lights
> My friend sent me a series of flashing lights... I think he was trying to tell me something... I've copied them down for you, can you help me decode it?

Convert the emojis to binary. This can be done with a script or with an online text replacer ([for the lazy](http://www.unit-conversion.info/texttools/replace-text/)). Decode the binary.

Flag: `flag{C@N_UND3R$7AND?}`


## Is this art?
If we play with filters on [Forensically](https://29a.ch/photo-forensics/), we see some words in the middle of the image.

![](images/isthisart.PNG)

Flag: `ictf{!NV1$IBL3_BU7_N07_IM@G1N@RY}`


## Fuzzy
> My friend was rocking out to this music. It didn't seem like real music... He told me that the music was "super special." Can you help me figure it out?

If we listen to the file, do `strings`, and check the metadata, we don't find anything particularly interesting. Open the given .wav file in Audacity and change the view type to Spectrogram to get the flag.

![](images/fuzzy.PNG)

Flag: `ictf{W@V3S_@R3_F1@G$}`


## Factors
> Try to find the smallest positive integer number with 50 factors! Its not that easy... 

ah yes google ~~math is just osint~~

good link: https://rosettacode.org/wiki/Sequence:_smallest_number_with_exactly_n_divisors#J

anyway.

Flag: `ictf{6480}`


## Colors
> I found this cool strip of colors! It looks pretty nice, but they all seem rather dull. It almost seems as if its speaking a message! Maybe you could help me find it?

![](images/colors.png)

Colors can generally be represented using hex codes, which we can then convert into text. I used [this tool](https://htmlcolorcodes.com/) to extract the hex codes, which, when converted to ASCII, gave us the flag.

Flag: `ictf{h3x_c01ors!}`