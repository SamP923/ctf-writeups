# You can install these packages to help w/ solving unless you have others in mind
# i.e. python3 -m pip install {name of package}
from pwn import *
import codecs
from base64 import b64decode
from string import ascii_lowercase

HOST = 'chal.ctf.b01lers.com'
PORT = 2008

r = remote(HOST,PORT)

lookup = {'A': 'aaaaa', 'B': 'aaaab', 'C': 'aaaba', 'D': 'aaabb', 'E': 'aabaa',
          'F': 'aabab', 'G': 'aabba', 'H': 'aabbb', 'I': 'abaaa', 'J': 'abaab',
          'K': 'abaab', 'L': 'ababa', 'M': 'ababb', 'N': 'abbaa', 'O': 'abbab',
          'P': 'abbba', 'Q': 'abbbb', 'R': 'baaaa', 'S': 'baaab', 'T': 'baaba',
          'U': 'babaa', 'V': 'babab', 'W': 'babaa', 'X': 'babab', 'Y': 'babba',
          'Z': 'babbb', ' ': ' '}

def bacon(s):
    # Do this
	plaintext = []
    i = 0
    reverse_cipher = {v: k for k, v in cipher.items()}
    # emulating a do-while loop
    while True:
        # condition to run decryption till the last set of ciphertext
        if i < len(message) - 4:
            # extracting a set of ciphertext from the message
            substr = message[i:i + 5]
            # checking for space as the first character of the substring
            if substr[0] != ' ':
                # This statement gets us the key(plaintext) using the values(ciphertext)
                # Just the reverse of what we were doing in encrypt function
                plaintext.append(reverse_cipher[substr])
                i += 5  # to get the next set of ciphertext
            else:
                # adds space
                plaintext.append(' ')
                i += 1  # index next to the space
        else:
            break  # emulating a do-while loop

    return ''.join(plaintext)

	
def rot13(s):
    # And this
	return codecs.encode(s, 'rot_13')
	
def atbash(s):
    # And this one
	N = ord('z') + ord('a')
    ans=''
    return ans.join([chr(N - ord(s)) for s in text])
	
def Base64(s):
    # Lastly this one
	return base64.b64decode(s)
	
if __name__ == '__main__':
    count = 0
    while True:     
        r.recvuntil('Method: ')
        method = r.recvuntil('\n').strip()
        r.recvuntil('Ciphertext: ')
        argument = r.recvuntil('\n').strip()

        result = globals()[method.decode()](argument.decode())  # :)

        r.recv()
        r.sendline(result.encode())
        count += 1
        if count == 1000:
            print(r.recv())
            exit(0)
    
