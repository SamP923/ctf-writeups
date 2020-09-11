# Forensics
10/?
- Glory of the Garden, 50 Points
- unzip, 50 Points
- So Meta, 150 Points
- What Lies Within, 150 Points
- Extensions, 150 Points
- shark on wire 1, 150 Points
- WhitePages, 250 Points
- c0rrupt, 250 Points
- like1000, 250 Points
- shark on wire 2, 300 Points

## Glory of the Garden
> This garden contains more than it seems. You can also find the file in /problems/glory-of-the-garden_6_0d6d3ea97757b84c7a51a38daa7dca8d on the shell server.

Hint asks us "What is a hex editor?" So we open it in a [hex editor](https://hexed.it/) and find the flag at the bottom of the file.  
Flag: `picoCTF{more_than_m33ts_the_3y3f20F5be9}`


## unzip
> Can you unzip this file and get the flag?

Unzip the file. Image inside has the flag.
Flag: `picoCTF{unz1pp1ng_1s_3a5y}`.


## So Meta
> Find the flag in this picture. You can also find the file in /problems/so-meta_3_6dc950904c3ee41f324ae8d9f142f2b8.

We can use ExifTool on the shell to look at the metadata.
```
$ exiftool pico_img.png
```
We see this line
```
Artist                          : picoCTF{s0_m3ta_43f253bb}
```
Flag: `picoCTF{s0_m3ta_43f253bb}`


## What Lies Within
> Theres something in the building. Can you retrieve the flag?

Looking at the metadata using [exiftool](https://www.metadata2go.com/) gives us what looks like hex...
```
Raw Header:
89 50 4E 47 0D 0A 1A 0A 00 00 00 0D 49 48 44 52 00 00 02 91 00 00 01 B6 08 06 00 00 00 27 6A DD D8 00 00 20 00 49 44 41 54 78 5E AC BD 4D 8B 24 6B 96 26 76 D2 CA DA DA DA CA DA 70 B9 5C 2E C7
```
uhh hex gives us some weird things, so I searched up "online image decoder" which gave me this helpful [image decoder](https://stylesuxx.github.io/steganography/)  
Flag: `picoCTF{h1d1ng_1n_th3_b1t5}`

## Extensions
> This is a really weird text file TXT? Can you find the flag?

Description text suggests that the file extension may have been changed. Changing it to a .png file gives us an image with the flag.  
Flag: `picoCTF{now_you_know_about_extensions}`

## shark on wire 1
> We found this packet capture. Recover the flag. You can also find the file in /problems/shark-on-wire-1_0_13d709ec13952807e477ba1b5404e620.

Sharks on a wire... wireshark. Hint asks us "What are streams?" With Wireshark, you're able to look at TCP and UDP streams. Looked through TCP, didn't find anything. Found some malformed packets on the 5th UDP stream that had "pico" on it, but this just lead to "picopicopicopico."
Follow on a packet from the 6th stream
Flag: `picoCTF{StaT31355_636f6e6e}`  
Checking the 7th stream gives us: picoCTF{N0t_a_fLag}


## WhitePages
> I stopped using YellowPages and moved onto WhitePages... but the page they gave me is all blank!

Since we can highlight things, we know that the text is entirely composed of whitespace characters. There didn't seem to be a converter online (because who would make one), but doing a CTRL+F shows that there's spaces in the file.
```
for (int i = 0; i < plaintext.length(); i++){
      if ( plaintext.charAt(i) == ' ') System.out.print(1);
      else System.out.print(0);
}
```
gives us binary, which, when converted to ascii gives us
```
		picoCTF

		SEE PUBLIC RECORDS & BACKGROUND REPORT
		5000 Forbes Ave, Pittsburgh, PA 15213
		picoCTF{not_all_spaces_are_created_equal_dd5c2e2f77f89f3051c82bfee7d996ef}
```
Flag: `picoCTF{not_all_spaces_are_created_equal_dd5c2e2f77f89f3051c82bfee7d996ef}`


## c0rrupt
> We found this file. Recover the flag. You can also find the file in /problems/c0rrupt_0_1fcad1344c25a122a00721e4af86de13.
> Hint: Try fixing the file header

Using EXIFTOOl, the header is 
```
89 65 4E 34 0D 0A B0 AA 00 00 00 0D 43 22 44 52 00 00 06 6A 00 00 04 47 08 02 00 00 00 7C 8B AB 78 00 00 00 01 73 52 47 42 00 AE CE 1C E9 00 00 00 04 67 41 4D 41 00 00 B1 8F 0B FC 61 05 00 00

```
Kind of looks like that .PNG file from earlier, so I guess it's a PNG. Googling "how to fix file headers" suggests that [replace the header of the affected file with the header from a healthy file](https://www.nucleustechnologies.com/blog/how-to-fix-broken-or-corrupt-jpeg-file-headers/). The Wikipedia page for [PNG headers](https://en.wikipedia.org/wiki/Portable_Network_Graphics#File_header) tells us that all PNGs must start with the line
```
89 50 4E 47 0D 0A 1A 0A
```
which is different from our original. Changing this alone didn't work :/
Cross-referencing a healthy PNG file and looking for the critical chunks needed to open a PNG, opening the entire file in a hex editor and fixing it to have IDHR and IDAT spelled correctly were enough to open the image that contained the flag.
```
89 65 4E 34 0D 0A B0 AA became
89 50 4E 47 0D 0A 1A 0A

43 22 44 52 became
49 48 44 52

AB 44 45 54 became
49 44 41 54
```
Flag: `picoCTF{c0rrupt10n_1847995}`

## like1000
> This .tar file got tarred alot. Also available at /problems/like1000_0_369bbdba2af17750ddf10cc415672f1c.

uhh scripting
```
import os

for i in range (1000, 0, -1):
	# x - extract, p - preserve the details/permissions, f - create an archive file
	os.system("tar xpf " + str(i) + ".tar")
	# remove the previous tar file
	os.system("rm " + str(i+1)+".tar")
```
This outputs 1.tar, filler.txt, and flag.png.
Flag: `picoCTF{l0t5_0f_TAR5}`

## m00nwalk
> Decode this message from the moon. You can also find the file in /problems/m00nwalk_5_72c1b4e13cc7ddd43d7fb3b0ae86afef.


## shark on wire 2
> We found this packet capture. Recover the flag that was pilfered from the network. You can also find the file in /problems/shark-on-wire-2_0_3e92bfbdb2f6d0e25b8d019453fdbf07.

Looking through the UDP streams again, we come across weird headers that contain `start` and `end`. Looking at just the ones from port 22, we take the source ports and get
```
5000 5112 5105 5099 5111 5099 5111 5067 5084 5070 5123 5112 5049 5076 5076 5102 5051 5114 5051 5100 5095 5100 5097 5116 5097 5095 5118 5049 5097 5095 5115 5116 5051 5103 5048 5125 5000
```
This ends up being decimal encoding when you remove the 5's, which, when converted to ASCII, gives you the flag.
```
0 112 105 99 111 67 84 70 123 112 49 76 76 102 51 114 51 100 95 100 97 116 97 95 118 49 97 95 115 116 51 103 48 125 0
```
Flag: `picoCTF{p1LLf3r3d_data_v1a_st3g0}`

