f1 = open("output.txt", "wb")

with open("challenge.enc", "rb") as f2:
	data = f2.read()

data_1 = data[::-1]

f1.write(data_1)
f1.close()
