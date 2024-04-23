from math import sqrt

sq = 0
sqt = 0
cube = 0
fourth = 0

for i in range(0, 21):
  sq = i ** 2
  sqt = round(sqrt(i), 4)
  cube = i ** 3
  fourth = round(sqrt(sqt), 4)
  print(i, " ", sq, " ", sqt, " ", cube, " ", fourth)