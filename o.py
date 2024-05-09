import time
def clear():
  for i in range(40):
    print()
O = 1
o = 0
changeO = 1
changeo = 1
spaceO = ''
Oo = 1
while True:
  spaceO = ' '*o
  if Oo == 1: print(spaceO + 'o')
  if Oo == -1: print(spaceO + 'O')
  for i in range(O):
    print()
  
  if O == 39:
    changeO = -1
  if O == 0:
    changeO = 1
  if o == 50:
    changeo = -1
  if o == 1:
    changeo = 1
  
  time.sleep(0.1)
  clear()
  O += changeO
  o += changeo
  Oo *= -1