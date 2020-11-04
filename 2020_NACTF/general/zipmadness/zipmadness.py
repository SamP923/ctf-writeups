import os

for i in range(999,0,-1):
    direction = open('direction.txt').read()
    os.system("rm direction.txt")
    os.system("unzip " + str(i) + direction + ".zip")
    os.system("rm " + str(i+1) + "left.zip "+ str(i+1) + "right.zip")
    
