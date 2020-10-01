## WASM
> Find my flag... It's hidden in memory!

> https://digitalmortifiedactivecell.mendel3.repl.co/

> Hints: https://stackoverflow.com/questions/51562325/webassembly-correct-way-to-get-a-string-from-a-parameter-with-memory-address

> https://marcoselvatici.github.io/WASM_tutorial/

I don't think this was the intended way to solve, especially given the first hint, but it was easy to understand and execute. We're told to search through the memory, and the second hint references the `getValue` function.

The following code checks through all values in WASM memory, sees if they are not 0, checks if the decimal corresponds to a printable ASCII character, then prints it. This is then printed to the Javacript console.

```
var i;
for (i = 0; i < Module.HEAP8.byteLength; i++){
    var val = getValue(i, "i8");
    if ( val != 0 && val >= 33 && val <= 127) {
        console.log(getValue(i, "i8"));
    }
}
```

Converting that decimal output to ASCII using RapidTables we get
> msc'-&:6q/%r3.4tl6q3p%lq'l6t,<%sIlefÓheflagheresomewarebutIcan'trememberwhereIputit.Couldyousearchthroughmymemoryandfindit?-+0X0x(nuÒ)0123456789ABCDEF-0X+0X0X-0x+0x0xinfINFnanNAN.XgTsX!s!$!flag{w0nd3rou5-w0r1d-0f-wa5m}'-&:6q/%r3.4tl6q3p%lq'l6t,<./this.programP

Flag: `flag{w0nd3rou5-w0r1d-0f-wa5m}`
