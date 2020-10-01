import random

random.seed(12)

flag = "**REDACTED**"
ciphertext = ""

for n in flag:
    ciphertext += str(random.randint(1,100) ^ ord(n)) + " "

print(ciphertext)
