f = open('flag.txt').read().split()

def is_fr_valid(s):
    al = 'nac'
    for i in s:
        if i not in al:
            return False
    return True

def is_bk_valid(s):
    al = 'ctf'
    for i in s:
        if i not in al:
            return False
    return True

for i in f:
    if len(i) == 52 and is_fr_valid(i[6:16]) and is_bk_valid(i[-15:-1]):
        print(i)
    
print('done')
