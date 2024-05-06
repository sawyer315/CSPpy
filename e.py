import time
print('EeEeE')
es = 1
bigE = 1
littleE = 0
space = es
countE = 1
E_is_the_best_letter = True
while E_is_the_best_letter:
  space = ' '*es + ' '* (littleE%4)
  print(space+'e')
  es += bigE
  if es == 25:
    bigE = -1
  if es == 1:
    bigE = 1
  littleE += 1
  littleE *= -1
  time.sleep(0.1)
  if littleE == 400:
    print('aahhhhhhhh')
  if countE%100 == 0 :
    linE = 'eeeeeeeeeeeeeeeeeeeee'
    shortE = 'ee'
    print(linE)
    print(linE)
    print(shortE)
    print(shortE)
    print(shortE)
    print(shortE)
    print(shortE)
    print(shortE)
    print(shortE)
    print(linE)
    print(linE)
    print(shortE)
    print(shortE)
    print(shortE)
    print(shortE)
    print(shortE)
    print(shortE)
    print(shortE)
    print(linE)
    print(linE)
  countE +=1