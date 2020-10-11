## Save Trees!
> Hi! Can you help me saving this little tree?

We've given a fairly large file that has lot of nested sections called "SimpleStatementLine"s. If we take a look at the pattern, a lot of this is junk, but we do see in every section an Integer given a certain value. This gives us
```
11,34,9,59,90,157,153,154,185,92,157,26,153,153,155,94
```

At first, the two and three numbers might look like a decimal to ASCII conversion, but some of the numbers fall outside of the printable ASCII character codes. If we notice the string in the first section, it's actually 215 characters long. Let's write a short program to figure out if these numbers correspond to letters in the string, which could give us our flag.

```
int[] numArr = {11, 34, 9,59,90,157,153,154,185,92,157,26,153,153,155,94};
    
String str = "hey guys this is a leet string which is not related to the flag. Also dont search for ictf{?_?} stuff, you wont find any :) Lets count till 10, right? 123456789. No!! You forgot the 0! Muahahaha! Im tired of this XD";

String pt = "";
for (int i = 0; i < numArr.length; i++){
	pt += str.charAt(numArr[i]);
}

System.out.println(pt);
```

It does. Nice!

Flag: `ictf{734M_7r335}`