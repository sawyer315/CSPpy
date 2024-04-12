msg = str(input('Message: '))
key = bin(int(input('Key: ')))
list = []

while len(msg) % 5 != 0:
  msg+=' '

for char in msg:
  list.append(bin(ord(char)-32))

print(list)
print(len(list[0]))
