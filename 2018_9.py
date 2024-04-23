def XOR(code,key,iter):
  out = ''
  bit = iter
  for char in code:
    if char != key[bit]:
      out += '1'
    else:
      out += '0'
    bit +=1
    if bit >29: bit = 0
  return out
binary = str(input('Code? '))
num = int(input('Key? '))
key = bin(num).lstrip('0b')
while len(key) < 30:
  key = '0' + key
print(key)
while len(binary) % 5 != 0:
  binary += ' '
list = []
list2 = []
fives = []
for char in binary:
  temp = ord(char)-32
  list.append(temp)
print(list)
for item in list:
  temp = bin(item).lstrip('0b')
  while len(temp) < 6:
    temp = '0' + temp
  list2.append(temp)
print(list2)

for i in range(0, len(list2), 5):
  fives.append(list2[i]+list2[i+1]+list2[i+2]+list2[i+3]+list2[i+4])
print(fives)
encoded = []
for item in fives:
  encoded.append(XOR(item, key, fives.index(item)))
print(encoded)

newbins = []
for item in encoded:
  newbins.append(item[0]+item[1]+item[2]+item[3]+item[4]+item[5])
  newbins.append(item[6]+item[7]+item[8]+item[9]+item[10]+item[11])
  newbins.append(item[12]+item[13]+item[14]+item[15]+item[16]+item[17])
  newbins.append(item[18]+item[19]+item[20]+item[21]+item[22]+item[23])
  newbins.append(item[24]+item[25]+item[26]+item[27]+item[28]+item[29])
print(newbins)

ords = []
for item in newbins:
  temp = 0
  if item[0] == '1':
    temp += 32
  if item[1] == '1':
    temp += 16
  if item[2] == '1':
    temp += 8
  if item[3] == '1':
    temp += 4
  if item[4] == '1':
    temp += 2
  if item [5] == '1':
    temp += 1
  temp += 32
  ords.append(temp)

print(ords)
final = ''
for item in ords:
  final += chr(item)
print(final)