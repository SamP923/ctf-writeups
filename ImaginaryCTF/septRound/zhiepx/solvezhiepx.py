import binascii

with open('zhiepx', 'r') as f1:
  lines = f1.readlines()

with open('output.png', 'wb') as f2:
  for line in lines:
    line = line[10:-20].replace(" ", "")
    f2.write(binascii.a2b_hex(line))
  





