# General Skills
17/17
- The Factory's Secret, 1 Point
- 2Warm, 50 Points
- Lets Warm Up, 50 Points
- Warmed Up, 50 Points
- Bases, 100 Points
- First Grep, 100 Points
- Resources, 100 Points
- strings it, 100 Points
- what's a net cat?, 100 Points
- Based, 200 Points
- First Grep: Part II, 200 Points
- plumbing, 200 Points
- whats-the-difference, 200 Points
- where-is-the-file, 200 Points
- flag_shop, 300 Points
- mus1c, 300 Points
- 1_wanna_b3_a_r0ck5tar, 350 Points


## where-is-the-file
> I've used a super secret mind trick to hide this file. Maybe something lies in /problems/where-is-the-file_2_f1aa319cafd4b55ee4a60c1ba65255e2.
```
$ ls -a
$ cat .cant_see_me
```
Flag: `picoCTF{w3ll_that_d1dnt_w0RK_30444bc6}`


## flag_shop
> There's a flag shop selling stuff, can you buy a flag? Source. Connect with nc 2019shell1.picoctf.com 60851.
This is a flag shop! We start with a balance of 1100, which is not enough for the 1337 Flag. Since it only looks if we input 1, we have to find somewhere else to adjust the account balance. What happens if we try to buy a knockoff flag?
```
if(auction_choice == 1){
    printf("These knockoff Flags cost 900 each, enter desired quantity\n");
                
    int number_flags = 0;
    fflush(stdin);
    scanf("%d", &number_flags);
    if(number_flags > 0){
         int total_cost = 0;
         total_cost = 900*number_flags;
         printf("\nThe final cost is: %d\n", total_cost);
         if(total_cost <= account_balance){
             account_balance = account_balance - total_cost;
             printf("\nYour current balance after transaction: %d\n\n", account_balance);
         }
         else{
             printf("Not enough funds to complete purchase\n");
         }
     }
}
```

We can see that it calculates the total cost of flags and stores it as an integer. Then, it checks if the total_cost is less than or equal to the account balance. Integers are capped from -2,147,483,647 to 2,147,483,647. This means if we overflow the highest number, our total cost should turn to a negative number, which when then give us a massive account balance. 
```
2147483648/900 = 2386092.942 
2386093 is our minimum overflow number
```
Enter the value when asked how many knockoff flags we want, get flag.
Flag: `picoCTF{m0n3y_bag5_34c9a5f7}`

## mus1c
> I wrote you a song. Put it in the picoCTF{} flag format

Using rockstar's [online compiler](https://codewithrockstar.com/online), we can run this code, which prints
```
114
114
114
111
99
107
110
114
110
48
49
49
51
114
```
Three letters usually means ASCII, so we convert the decimal numbers to ASCII and get our flag.

Flag: `picoCTF{rrrocknrn0113r}`


## 1_wanna_b3_a_r0ck5tar
> I wrote you another song. Put the flag in the picoCTF{} flag format

So we've got another rockstar code snippet. I went and read the docs and it made me sad. Separating out the lines of code so the print statements would actually print (most of it is enclosed in an if-if-else statement) gives you a string of decimal numbers, which can then convert to ASCII to get the flag.
```
Rocknroll is right              
Silence is wrong                
A guitar is a six-string        
Tommy's been down               
Music is a billboard-burning razzmatazz!

# rocknroll = true
# silence = false
# guitar = 10
# Tommy = 44
# Music = 170

Listen to the music             
If the music is a guitar                  
Say "Keep on rocking!" 

# if music = guitar
# print("keep on rocking")
               
Listen to the rhythm
If the rhythm without Music is nothing

Tommy is rockin guitar
Shout Tommy!
                    
Music is amazing sensation 
Jamming is awesome presence
Scream Music!                   
Scream Jamming!               

Tommy is playing rock           
Scream Tommy!       

They are dazzled audiences                  
Shout it!

Rock is electric heaven                     
Scream it!

Tommy is jukebox god            
Say it!      
                               
Break it down
Shout "Bring on the rock!"
(Else Whisper "That ain't it, Chief")                
Break it down 
```
Flag: `picoCTF{BONJOVI}`

