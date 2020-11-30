s = input("Enter your secret: ")
res = ''.join(format(ord(i), 'b') for i in s)
print("Ciphertext: " + res)