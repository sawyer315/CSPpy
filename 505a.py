file = open("data/prog505a.txt", "r")
per1 = file.readline(1)
per2 = file.readline(2)
per3 = file.readline(3)
per4 = file.readline(4)
per5 = file.readline(5)

for char in per1:
  if char.isnumeric() == true:
    books1 = char

for char in per2:
  if char.isnumeric() == true:
    books2 = char

for char in per3:
  if char.isnumeric() == true:
    books3 = char

for char in per4:
  if char.isnumeric() == true:
    books4 = char

for char in per5:
  if char.isnumeric() == true:
    books5 = char

def points(books):
  out = 0
  for i in range(0, books - 1):
    if i <= 2:
      out += 10
    elif i <= 5:
      out += 15
    else:
      out += 20
    return out

