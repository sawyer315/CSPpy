import time
print('EeEeE')
es = 1
bigE = 1
littleE = 0
space = es
while True:
  space = ' '*es + ' '* (littleE%3)
  print(space+'e')
  es += bigE
  if es == 20:
    bigE = -1
  if es == 1:
    bigE = 1
  littleE += 1
  littleE *= -1
  time.sleep(0.1)