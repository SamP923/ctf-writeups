f = open('sum.txt', 'r')

lines = f.readlines()

sum = 0

for line in lines:
    sum+=int(line)

print("sum: ", sum)
