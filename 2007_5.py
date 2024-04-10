string = str(input('String: '))
list = []
for char in string:
  list.append(char)
string = ''
for item in list:
  if item == item[list.index(item)+1]:
    string += item
  else:
    string += item
    string += ' '

print(string)