## Not So Easy Binary Decode
> Little Timmy always admired hackers so he made a program to encrypt his lucky NUMBER using binary.
> However, he forgot to make the decryption program and now he can't decode his lucky NUMBER.
> Maybe you can help him?
> You should submit flag{decrypted_string} as the flag

We're heavily hinted that the flag is a number. Numbers in binary are only 6 bits long, so we can either pad the front of each 6-bit group with two zeros and put it in a decoder or just take substrings in intervals of 6. 

```
class Main {
  public static void main(String[] args) {
    String ct = "110010111001110011110011110111111001110000110100110001110101110111110011110001110001111000110000110100110101111001110100110010110001110111111000110000110110110010110100110101110101111000111001110001110001110001110101110110111000110011111001110011111001110110110000110101110100110010111001110000110110110011110001110010110110110010110101110000110011110111110100110110110011110010111000110101110100";

    String pt ="";
    for (int i = 0; i < ct.length(); i +=6){
      int charCode = Integer.parseInt(ct.substring(i, i+6), 2);
      pt = pt + new Character((char)charCode).toString();
    }

    System.out.println("flag{" + pt + "}");
  }
}
```


Flag: `flag{293379041573118045942178062455891115683939605429063126250374632854}`