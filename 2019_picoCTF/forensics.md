# Forensics
- Glory of the Garden, 50 Points
- unzip, 50 Points
- So Meta, 150 Points
- Extensions, 150 Points

## Glory of the Garden
### Description
> This garden contains more than it seems. You can also find the file in /problems/glory-of-the-garden_6_0d6d3ea97757b84c7a51a38daa7dca8d on the shell server.

### Solution: 
Hint asks us "What is a hex editor?" So we open it in a [hex editor](https://hexed.it/) and find the flag at the bottom of the file.
Flag: `picoCTF{more_than_m33ts_the_3y3f20F5be9}`


## unzip
### Description
> Can you unzip this file and get the flag?

### Solution: 
Unzip the file. Image inside has the flag.
Flag: `picoCTF{unz1pp1ng_1s_3a5y}`.


## So Meta
### Description
> Find the flag in this picture. You can also find the file in /problems/so-meta_3_6dc950904c3ee41f324ae8d9f142f2b8.

### Solution: 
We can use ExifTool on the shell to look at the metadata.
```
$ exiftool pico_img.png
```
We see this line
```
Artist                          : picoCTF{s0_m3ta_43f253bb}
```
Flag: `picoCTF{s0_m3ta_43f253bb}`


## Extensions
### Description
> This is a really weird text file TXT? Can you find the flag?

### Solution: 
Description text suggests that the file extension may have been changed. Changing it to a .png file gives us an image with the flag.
Flag: `picoCTF{now_you_know_about_extensions}`