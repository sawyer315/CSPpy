res = int(input('Starting oz: '))
order = str(input('Order: '))
list = order.split()
[int(x) for x in list]
filled = True
num = 0

while filled is True:
  if list != [] and res - (int(list[0])+1) >=0:
    res -= (int(list[0])+1)
    list.remove(list[0])
    num+=1
  else:
    filled = False

print(f'Filled {num} cups.')