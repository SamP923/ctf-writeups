# General Skills
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
- mus1c, 300 Points
- 1_wanna_b3_a_r0ck5tar, 350 Points

## 1_wanna_b3_a_r0ck5tar
### Description
> I wrote you another song. Put the flag in the picoCTF{} flag format

### Solution
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


## Title of problem
### Description
> Description of problem

### Solution
Flag: `picoCTF{}`

