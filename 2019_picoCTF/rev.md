# Reverse Engineering
- vault-door-training, 50 Points
- vault-door-1, 100 Points
- asm1
- vault-door-3, 200 Points
- vault-door-4, 250 Points
- vault-door-5, 300 Points
- vault-door-6, 350 Points

## asm1
### Description
> What does asm1(0x4f3) return? Submit the flag as a hexadecimal value (starting with '0x'). NOTE: Your submission for this question will NOT be in the normal flag format. Source located in the directory at /problems/asm1_6_74dd61bdf487805bf057c71be7941289.
```
<+0>:   push   ebp
        <+1>:   mov    ebp,esp
        <+3>:   cmp    DWORD PTR [ebp+0x8],0x45d
        <+10>:  jg     0x512 <asm1+37>
        <+12>:  cmp    DWORD PTR [ebp+0x8],0x430
        <+19>:  jne    0x50a <asm1+29>
        <+21>:  mov    eax,DWORD PTR [ebp+0x8]
        <+24>:  add    eax,0x17
        <+27>:  jmp    0x529 <asm1+60>
        <+29>:  mov    eax,DWORD PTR [ebp+0x8]
        <+32>:  sub    eax,0x17
        <+35>:  jmp    0x529 <asm1+60>
        <+37>:  cmp    DWORD PTR [ebp+0x8],0x7cd
        <+44>:  jne    0x523 <asm1+54>
        <+46>:  mov    eax,DWORD PTR [ebp+0x8]
        <+49>:  sub    eax,0x17
        <+52>:  jmp    0x529 <asm1+60>
        <+54>:  mov    eax,DWORD PTR [ebp+0x8]
        <+57>:  add    eax,0x17
        <+60>:  pop    ebp
        <+61>:  ret
```

### Solution
I used a [hexadecimal converter](https://www.hexadecimaldictionary.com/hexadecimal/).
`0x4f3` = 1267, which is what we pass to the asm file. The first `cmp` compares it to `0x45d` or 1117. `jg` is a jump if the value is greater, which it is, so we jump to `+37`. This compares 1267 to `0x7cd`, or 1997. With `jne`, we jump if the operands are not equal, so we jump to `+54`. This then adds 0x17 to our original value, which gives us our flag.

Flag:`0x50a`

## vault-door-6
### Description
> This vault uses an XOR encryption scheme. The source code for this vault is here: VaultDoor6.java

### Solution
To reverse an XOR, we shift it by the same value again (X^Y=Z, then Z^Y=X). In this case, X is the `myBytes`, Y is the shift `0x55`, and Z is `myBytes`.
```
  public static void solve(){
    byte[] passBytes = new byte[32];
    byte[] myBytes = {
      0x3b, 0x65, 0x21, 0xa , 0x38, 0x0 , 0x36, 0x1d,
      0xa , 0x3d, 0x61, 0x27, 0x11, 0x66, 0x27, 0xa ,
      0x21, 0x1d, 0x61, 0x3b, 0xa , 0x2d, 0x65, 0x27,
      0xa , 0x34, 0x30, 0x31, 0x30, 0x36, 0x30, 0x31,
    };
    for (int i=0; i<32; i++) {
      passBytes[i] = (byte) (myBytes[i] ^ 0x55); 
      System.out.print(passBytes[i] + " ");
    }
  }
```
Flag:`picoCTF{n0t_mUcH_h4rD3r_tH4n_x0r_aedeced}`


## Title of problem
### Description
> Description of problem

### Solution
Flag:`picoCTF{}`

