import time
bigA = ''
changeA = 4
while True:
  single = 'a'
  double = 'aa'
  sspace = '         '
  dspace1 = '      '
  dspace2 = '   '
  
  while len(single) != 7:
    print(bigA+sspace+single+sspace)
    single += 'aa'
    sspace = (len(sspace)-1)*' '
  
  while len(dspace2) != 9:
    print(bigA+dspace1+double+dspace2+double+dspace1)
    dspace1 = (len(dspace1)-1)*' '
    dspace2 = (len(dspace2)+2)*' '
  single = (13*'a')
  sspace = (3*' ')
  while len(single) != 17:
    print(bigA+sspace+single+sspace)
    single += 'aa'
    sspace = (len(sspace)-1)*' '
  
  dspace2 = (' '*13)
  dspace1 = ' '
  while len(dspace2) != 17:
    print(bigA+dspace1+double+dspace2+double+dspace1)
    dspace1 = (len(dspace1)-1)*' '
    dspace2 = (len(dspace2)+2)*' '
  if changeA == 4: bigA += changeA*' '
  if changeA == -4: bigA = (len(bigA)-4)*' '
  
  if len(bigA) > 46: changeA = -4
  if bigA == '': changeA = 4
  time.sleep(0.1)
