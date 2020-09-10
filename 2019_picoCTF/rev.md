# Reverse Engineering
- vault-door-training, 50 Points
- vault-door-1, 100 Points
- asm1, 200 Points
- vault-door-3, 200 Points
- asm2, 250 Points
- vault-door-4, 250 Points
- asm3, 300 Points
- vault-door-5, 300 Points
- vault-door-6, 350 Points
- vault-door-7, 400 Points
- vault-door-8, 450 Points

## vault-door-training

## vault-door-1

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

## vault-door-3

## asm2
### Description
> What does asm2(0xe,0x22) return? Submit the flag as a hexadecimal value (starting with '0x'). NOTE: Your submission for this question will NOT be in the normal flag format. Source located in the directory at /problems/asm2_4_548389d70e48a3ca5473a24096f2186a.

```
	<+0>:	push   ebp
	<+1>:	mov    ebp,esp
	<+3>:	sub    esp,0x10
	<+6>:	mov    eax,DWORD PTR [ebp+0xc]
	<+9>:	mov    DWORD PTR [ebp-0x4],eax
	<+12>:	mov    eax,DWORD PTR [ebp+0x8]
	<+15>:	mov    DWORD PTR [ebp-0x8],eax
	<+18>:	jmp    0x50c <asm2+31>
	<+20>:	add    DWORD PTR [ebp-0x4],0x1
	<+24>:	add    DWORD PTR [ebp-0x8],0xd1
	<+31>:	cmp    DWORD PTR [ebp-0x8],0x9087
	<+38>:	jle    0x501 <asm2+20>
	<+40>:	mov    eax,DWORD PTR [ebp-0x4]
	<+43>:	leave  
	<+44>:	ret   
```

## Solution
So we start by moving our second input `ebp+0xc` into `eax`, then move this value into `ebp-0x4`. Then, we move our first input `ebp+0x8` into eax, then into `ebp-0x8`. We then have a loop that checks whether or not our first input is greater than `0x9087`. If not, then add `0x1` to `ebp-0x4` and add `0xd1` to `ebp-0x8`. This counts how many times `0xd1` needs to be added to the first input exceed `0x9087`.

Flag: `0xd3`

## vault-door-4

## asm3
### Description
> What does asm3(0xdff83990,0xeeff29ae,0xfa706498) return? Submit the flag as a hexadecimal value (starting with '0x'). NOTE: Your submission for this question will NOT be in the normal flag format. Source located in the directory at /problems/asm3_3_8aa3e17880273360f781adadc67a15f0.

```
.intel_syntax noprefix
.global asm3

asm3:
	<+0>:	push   ebp
	<+1>:	mov    ebp,esp
	<+3>:	xor    eax,eax
	<+5>:	mov    ah,BYTE PTR [ebp+0xb]
	<+8>:	shl    ax,0x10
	<+12>:	sub    al,BYTE PTR [ebp+0xd]
	<+15>:	add    ah,BYTE PTR [ebp+0xe]
	<+18>:	xor    ax,WORD PTR [ebp+0x12]
	<+22>:	nop
	<+23>:	pop    ebp
	<+24>:	ret   
```

### Solution
attempting to do it by hand :(
```
Set eax to 0
Mov `ebp+0xb` into `ah` (`0xc` is 2nd argument, so leftmost 2 digits of arg1 = `df`)

Shift `ax` left by `0x10` (`ax=0x0000`)

Subtract `ebp+0xd` from al (`0xd==0x29` 0x00-0x29 0xd7 or 0xd6...)

Add `ebp+0xe` to ah (`0xe==ff` + `0x00` = `0xff`)

eXclusive OR `ax` with `ebp+0x12` (`ebp+0x12==0xfa70`)
```

using c to solve
```
#include <stdio.h>

int main(void)
{
    printf("picoCTF{0x%x}\n", asm3(0xdff83990, 0xeeff29ae, 0xfa706498));
    return  0;
}
```

Flag: `0x5a7`


## reverse_cipher

## vault-door-5

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


## vault-door-7
### Description
> This vault uses bit shifts to convert a password string into an array of integers. Hurry, agent, we are running out of time to stop Dr. Evil's nefarious plans! The source code for this vault is here: VaultDoor7.java

### Solution
Can directly convert decimal values to hexadecimal, then to ASCII. Trying to convert decimal values to binary then to hex was awkward
Flag:`picoCTF{A_b1t_0f_b1t_sh1fTiNg_97cb1f367b}`

## vault-door-8
### Description
> Apparently Dr. Evil's minions knew that our agency was making copies of their source code, because they intentionally sabotaged this source code in order to make it harder for our agents to analyze and crack into! The result is a quite mess, but I trust that my best special agent will find a way to solve it. The source code for this vault is here: VaultDoor8.java

### Solution
When the code is cleaned up, you just reverse the order of the statements that the bits were switched in to unscramble.
```
public static char[] unscramble(){
    char[] a = { 0xF4, 0xC0, 0x97, 0xF0, 0x77, 0x97, 0xC0, 0xE4, 0xF0, 0x77, 0xA4, 0xD0, 0xC5, 0x77, 0xF4, 0x86, 0xD0, 0xA5, 0x45, 0x96, 0x27, 0xB5, 0x77, 0xA4, 0xF1, 0x94, 0xC1, 0xC0, 0xE1, 0xC1, 0xD1, 0x85 }; 
    for (int b=0; b<a.length; b++){
      char c = a[b]; 
      c = switchBits(c,6,7); 
      c = switchBits(c,2,5); 
      c = switchBits(c,3,4); 
      c = switchBits(c,0,1);
      c = switchBits(c,4,7);
      c = switchBits(c,5,6);
      c = switchBits(c,0,3);
      c = switchBits(c,1,2); 
      a[b] = c;
      System.out.print(c);
    }
    return a;
  }
```
Flag: `picoCTF{s0m3_m0r3_b1t_sh1fTiNg_b7a40645d}`