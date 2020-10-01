## Hello World!
> I​​​​‏​‍​​​​‏‌‎​​​​‎‏‍​​​​‏​‎​​​​‏‏‎​​​​‏‎​​​​​‏‎‍​​​​‏‍‍​​​​‏​‌​​​​‏‍‏​​​​‎‏​​​​​‏‎​​​​​‍​‌​​​​‎‏‏​​​​‏‍‏​​​​‏​‌​​​​‏‎‌​​​​‎‏​​​​​‏​‍​​​​‏‌‎​​​​‍​‍​​​​‏​‎​​​​‎‏​​​​​‏‎​​​​​‏‎‍​​​​‎‏‎​​​​‏‌‏​​​​‌‏‏​​​​‏‎‌​​​​‎‏​​​​​‏‎‌​​​​‏​‏​​​​‌‏‏​​​​‏‎​​​​​‎‏​​​​​‏​‍​​​​‌‏‎​​​​‏‍‏​​​​‎‏​​​​​‎‏‍​​​​‎‏​​​​​‏‎​​​​​‍​‌​​​​‎‏‏​​​​‏‍‏​​​​‍​‌​​​​‏‎‌​​​​‎‏​​​​​‍​‌​​​​‏‏​​​​​‏‎‌​​​​‏‍‏​​​​‍​‍​​​​‎‏​​​​​‎‏‏​​​​‏​‏​​​​‍​‍​​​​‏‌‎​​​​‏‌‎​​​​‍​‌​​​​‏‍​​​​​‏​‎​​​​‍​‌​​​‌​​​ forgot how to program, so I'll just type "Hello World". Much easier than making a program type it for me.

If we take a look at the file in a hex editor, there's a ton of characters between "H" and "ello World". We can see a repeating pattern of E2 80 8x, x being BCDEF. In unicode, we can see that these actual map to spaces -- more specifically, [zero-width spaces](https://www.utf8-chartable.de/unicode-utf8-table.pl?start=8192&number=128). We can use an online decoder like [zwsp-steg](https://github.com/offdev/zwsp-steg-js) to get our flag.

Flag: `flag{00pS_1_th0ught_th1s_w4s_4as1er}`

Taking the challenge text, we try that too for the 1337 secret challenge. 

Flag: `flag{super_s3cret_fl4g_subm1t_th1s_f0r_a_s3cr3t_3xtr4_ch4ll3ng3}`