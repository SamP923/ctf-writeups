# Cryptography
14/?
- The Numbers, 50 points
- 13, 100 points
- Easy1, 100 Points
- caesar, 100 Points
- Flags, 200 Points
- Mr-Worldwide, 200 Points
- Tapping, 200 Points
- la cifra de, 200 Points
- rsa-pop-quiz, 200 Points
- miniRSA, 300 Points
- b00tl3gRSA2, 400 Points
- waves over lambda, 300 Points

## The Numbers
> The numbers... what do they mean?
 
Image given. Convert numbers to letters based on ABC --> 123.  
Flag: `PICOCTF{THENUMBERSMASON}`

## 13
> Cryptography can be easy, do you know what ROT13 is? cvpbPGS{abg_gbb_onq_bs_n_ceboyrz}
 
As the name suggests, rotate the given flag by 13 characters.  
Flag: `picoCTF{not_too_bad_of_a_problem}`


## Easy1
> The one time pad can be cryptographically secure, but not when you know the key. Can you solve this? We've given you the encrypted flag, key, and a table to help UFJKXQZQUNB with the key of SOLVECRYPTO. Can you use this table to solve it?

Table clued in to it being a Vigenere cipher, used DCODE.  
Flag: `picoCTF{CRYPTOISFUN}`.  


## caesar
> Decrypt this message.
Download the file and you're given this:  
```
picoCTF{zolppfkdqeboryfzlktjxksyyl}
```
Name suggests caesar cipher, all 26 cases can be bruteforced using a script or DCODE to get the flag.  

Flag:`picoCTF{crossingtherubiconwmanvbbo}`


## Flags
> What do the flags mean?

Googling "flag decode" brings you to a [Maritime Signals Code decoder](https://www.dcode.fr/maritime-signals-code). Transcribe flags from the image to get the flag.  
Flag: `PICOCTF{F1AG5AND5TUFF}`


## Mr-Worldwide
> A musician left us a message. What's it mean?
```
picoCTF{(35.028309, 135.753082)(46.469391, 30.740883)(39.758949, -84.191605)(41.015137, 28.979530)(24.466667, 54.366669)(3.140853, 101.693207)_(9.005401, 38.763611)(-3.989038, -79.203560)(52.377956, 4.897070)(41.085651, -73.858467)(57.790001, -152.407227)(31.205753, 29.924526)}
```
The musician is Pitbull! Mr. Worldwide clues us in to that these numbers might be coordinates. Putting these coordinates into something like Google Maps gives us
```
(35.028309, 135.753082) - Kyoto, Japan
(46.469391, 30.740883)  - Odessa, Ukraine
(39.758949, -84.191605) - Dayton, Ohio
(41.015137, 28.979530)  - Istanbul, Turkey
(24.466667, 54.366669)  - Abu Dhabi, United Arab Emirates
(3.140853, 101.693207)  - Kuala Lumpur, Malaysia
			  _
(9.005401, 38.763611)   - Addis Ababa, Ethiopia
(-3.989038, -79.203560) - Loja, Ecuador
(52.377956, 4.897070)   - Amsterdam, Netherlands
(41.085651, -73.858467) - Sleepy Hollow, New York
(57.790001, -152.407227)- Kodiak, Alaska
(31.205753, 29.924526)  - Alexandria, Egypt
```

Flag: `picoCTF{KODIAK_ALASKA}`


## Tapping
> Theres tapping coming in from the wires. What's it saying nc 2019shell1.picoctf.com 21897.
```
.--. .. -.-. --- -.-. - ..-. { -- ----- .-. ... ...-- -.-. ----- -.. ...-- .---- ... ..-. ..- -. .---- ---.. .---- ---.. ..--- ..--- ....- ..... --... ..... }
```

Dots and dashes signal morse code. Decode to get the flag.
Flag: `PICOCTFM0RS3C0D31SFUN1818224575`


## la cifra de
> I  found this cipher in an old book. Can you figure out what it says? Connect with nc 2019shell1.picoctf.com 60147.
```
Ne iy nytkwpsznyg nth it mtsztcy vjzprj zfzjy rkhpibj nrkitt ltc tnnygy ysee itd tte cxjltk

Ifrosr tnj noawde uk siyyzre, yse Bnretèwp Cousex mls hjpn xjtnbjytki xatd eisjd

Iz bls lfwskqj azycihzeej yz Brftsk ip Volpnèxj ls oy hay tcimnyarqj dkxnrogpd os 1553 my Mnzvgs Mazytszf Merqlsu ny hox moup Wa inqrg ipl. Ynr. Gotgat Gltzndtg Gplrfdo 

Ltc tnj tmvqpmkseaznzn uk ehox nivmpr g ylbrj ts ltcmki my yqtdosr tnj wocjc hgqq ol fy oxitngwj arusahje fuw ln guaaxjytrd catizm tzxbkw zf vqlckx hizm ceyupcz yz tnj fpvjc hgqqpohzCZK{m311a50_0x_a1rn3x3_h1ah3xfmel1g3m}

Tnj qixxe wkqw-duhfmkseej ipsiwtpznzn uk l puqjarusahjeii htpnjc hubpvkw, hay rldk fcoaso 1467 be Qpot Gltzndtg Fwbkwei.

Zmp Volpnèxj Nivmpr ox ehkwpfuwp surptorps ifwlki ehk Fwbkwei Jndc uw Llhjcto Htpnjc.

It 1508, Ozhgsyey Ycizmpmozd itapnzjo tnj do-ifwlki eahzwa xjntg (f xazwtx uk dhokeej fwpnfmezx) ehgy hoaqo lgypr hj l cxneiifw curaotjyt uk ehk Atgksèce Inahkw.

Merqlsu’x deityd htzkrje avupaxjo it 1555 fd a itytosfaznzn uk ehk ktryy. Ehk qzwkw saraps uk ehk fwpnfmezx lrk szw ymtfzjo rklflgwwy, hze tnj llvmlbkyd ati ehk nydkc wezypry fce sniej gj mkfys uk l mtjxotnn kkd ahxfde, cmtcn hln hj oilkprkse woys eghs cuwceyuznjjyt.
```

Googling "La cifra de" brings up the Vigenere cipher Wikipedia page, as Battista Bellaso's book "La cifra del Sig." However, we don't have the key. Since we do know that `picoCTF` has to be in there somewhere, we can give a decoder the word, or use [one that does not need the key](https://www.guballa.de/vigenere-solver).

```
It is interesting how in history people often receive credit for things they did not create

During the course of history, the Vigenère Cipher has been reinvented many times

It was falsely attributed to Blaise de Vigenère as it was originally described in 1553 by Giovan Battista Bellaso in his book La cifra del. Sig. Giovan Battista Bellaso 

For the implementation of this cipher a table is formed by sliding the lower half of an ordinary alphabet for an apparently random number of places with respect to the upper halfpicoCTF{b311a50_0r_v1gn3r3_c1ph3rabef1b3b}

The first well-documented description of a polyalphabetic cipher however, was made around 1467 by Leon Battista Alberti.

The Vigenère Cipher is therefore sometimes called the Alberti Disc or Alberti Cipher.

In 1508, Johannes Trithemius invented the so-called tabula recta (a matrix of shifted alphabets) that would later be a critical component of the Vigenère Cipher.

Bellaso’s second booklet appeared in 1555 as a continuation of the first. The lower halves of the alphabets are now shifted regularly, but the alphabets and the index letters are mixed by means of a mnemonic key phrase, which can be different with each correspondent.
```
Flag: `picoCTF{b311a50_0r_v1gn3r3_c1ph3rabef1b3b}`


## waves over lambda
> We made alot of substitutions to encrypt this. Can you decrypt it? Connect with nc 2019shell1.picoctf.com 32282.
```
-------------------------------------------------------------------------------
hbadpjtu sxpx ku cblp znjd - zpxolxahc_ku_h_bmxp_njfevj_yttsttbelh
-------------------------------------------------------------------------------
extixxa lu tsxpx iju, ju k sjmx jnpxjvc ujkv ubfxisxpx, tsx ebav bz tsx uxj. exukvxu sbnvkad blp sxjptu tbdxtsxp tspblds nbad yxpkbvu bz uxyjpjtkba, kt sjv tsx xzzxht bz fjwkad lu tbnxpjat bz xjhs btsxp'u cjpaujav xmxa hbamkhtkbau. tsx njicxptsx exut bz bnv zxnnbiusjv, exhjlux bz sku fjac cxjpu jav fjac mkptlxu, tsx banc hluskba ba vxhw, jav iju nckad ba tsx banc pld. tsx jhhblatjat sjv epbldst blt jnpxjvc j ebr bz vbfkabxu, jav iju tbckad jphsktxhtlpjnnc ikts tsx ebaxu. fjpnbi ujt hpbuu-nxddxv pkdst jzt, nxjakad jdjkaut tsx fkggxa-fjut. sx sjv ulawxa hsxxwu, j cxnnbi hbfynxrkba, j utpjkdst ejhw, ja juhxtkh juyxht, jav, ikts sku jpfu vpbyyxv, tsx yjnfu bz sjavu bltijpvu, pxuxfenxv ja kvbn. tsx vkpxhtbp, ujtkuzkxv tsx jahsbp sjv dbbv sbnv, fjvx sku ijc jzt jav ujt vbia jfbadut lu. ix xrhsjadxv j zxi ibpvu njgknc. jztxpijpvu tsxpx iju uknxahx ba ebjpv tsx cjhst. zbp ubfx pxjuba bp btsxp ix vkv abt exdka tsjt djfx bz vbfkabxu. ix zxnt fxvktjtkmx, jav zkt zbp abtskad elt ynjhkv utjpkad. tsx vjc iju xavkad ka j uxpxaktc bz utknn jav xrolkuktx epknnkjahx. tsx ijtxp usbax yjhkzkhjnnc; tsx uwc, iktsblt j uyxhw, iju j exakda kffxauktc bz lautjkaxv nkdst; tsx mxpc fkut ba tsx xuuxr fjpus iju nkwx j djlgc jav pjvkjat zjepkh, slad zpbf tsx ibbvxv pkuxu kanjav, jav vpjykad tsx nbi usbpxu ka vkjysjablu zbnvu. banc tsx dnbbf tb tsx ixut, epbbvkad bmxp tsx lyyxp pxjhsxu, exhjfx fbpx ubfepx xmxpc fkaltx, ju kz jadxpxv ec tsx jyypbjhs bz tsx ula.
```

Waves and lambda point you to wavelengths and frequency. Using something like [quipqiup](https://www.quipqiup.com/), we can use frequency analysis to decrypt the message.

Flag: `picoCTF{frequency_is_c_over_lambda_ptthttobuc}`


## rsa-pop-quiz
> Given p and q, find n.

Multiply p and q.  
4636878989

> Given p and n, find q.

Divide n by q to find p.  
93089

> Given e and a very large n, find p and q.

Not possible given the factoring problem :(  
n

> Given p and q, calculate the totient.

Totient can be calculated using phi = (p-1)*(q-1).  
836623060

> Given plaintext, e, and n, produce a ciphertext.

Ciphertext = pow(pt, e, n)
256931246631782714357241556582441991993437399854161372646318659020994329843524306570818293602492485385337029697819837182169818816821461486018802894936801257629375428544752970630870631166355711254848465862207765051226282541748174535990314552471546936536330397892907207943448897073772015986097770443616540466471245438117157152783246654401668267323136450122287983612851171545784168132230208726238881861407976917850248110805724300421712827401063963117423718797887144760360749619552577176382615108244813

> Given ciphertext, smol e, and large n, deduce plaintext.

nope but apparently it was securely generate so  
n

> Given q, p, and e, produce d

d = inverse(e,phi)
1405046269503207469140791548403639533127416416214210694972085079171787580463776820425965898174272870486015739516125786182821637006600742140682552321645503743280670839819078749092730110549881891271317396450158021688253989767145578723458252769465545504142139663476747479225923933192421405464414574786272963741656223941750084051228611576708609346787101088759062724389874160693008783334605903142528824559223515203978707969795087506678894006628296743079886244349469131831225757926844843554897638786146036869572653204735650843186722732736888918789379054050122205253165705085538743651258400390580971043144644984654914856729

> Given p, ciphertext, e, n, produce plaintext

Solve for q, calculate totient, calculate d  
pt = pow(ct, d, n)  
14311663942709674867122208214901970650496788151239520971623411712977119642137567031494784893
