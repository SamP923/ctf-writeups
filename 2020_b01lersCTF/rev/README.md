## Thumb thumb
> Once upon a time, there was a young Thumb Thumb named Juni. Juni was shy and had no self confidence, until one day evil Thumb Thumbs kidnapped his spy Thumb Thumb Parents.
WANTED: EVIL THUMB THUMB. CRIME: KIDNAPPING. HAVE YOU SEEN THIS THUMB?

We're given a binary, so we open it in ghidra. The main function has four function calls. Investigating thumblings_assemble, there's an array of length 26 that stores a bunch of hex numbers. We reorganize to get our flag.

```
  local_78[0] = 0x66;
  local_78[1] = 0x6c;
  local_78[2] = 0x61;
  local_78[3] = 0x67;
  local_78[4] = 0x7b;
  local_78[5] = 0x73;
  local_78[6] = 0x33;
  local_78[7] = 0x6e;
  local_78[8] = 100;
  local_78[9] = 0x5f;
  local_78[10] = 0x30;
  local_78[11] = 0x75;
  local_78[12] = 0x72;
  local_78[13] = 0x5f;
  local_78[14] = 0x62;
  local_78[15] = 0x33;
  local_78[16] = 0x73;
  local_78[17] = 0x74;
  local_78[18] = 0x5f;
  local_78[19] = 0x74;
  local_78[20] = 0x68;
  local_78[21] = 0x75;
  local_78[22] = 0x6d;
  local_78[23] = 0x62;
  local_78[24] = 0x35;
  local_78[25] = 0x7d;
```
Flag: `flag{s3nd_0ur_b3st_thumb5}`

## Welcome to Game Over
> Welcome to the game, Shark Boy. I call the game....Game Over. Wait....shark boy isn't from this movie??? What?
You have a terminal and you have your wits. Find the exit. Good luck.

We're given a binary, so we open it in Ghidra. Skipping to the main function, we see the start of a flag. If we investigate the other functions, the only strange one is my_little_thumbling. Adding it to the segment we already have, we get our flag.

Flag: `flag{welc0me_to_th3_game_my_little_thumbling}`

## CrackMe
> You've done Reverse Engineering in C... Can you do it in Java?

See folder for reversing script.

Flag: `flag{J4V4_I$_th3_G04T}`