num = 1
while num != 0:
  num = int(input('What number? '))
  n = num
  factors = []
  delete = [1]
  for i in range(1, round(num / 2) + 1):
    if num % i == 0:
      factors.append(i)
  for item in factors:
    for i in range(2, item):
      if item % i == 0 and item not in delete:
        delete.append(item)
  for item in delete:
    factors.remove(item)
  if num == 2 or num == 3:
    factors.append(num)
  for item in factors:
    num *= (1 + (1 / item))
  print(factors)
  print(f'Psi of {n} = {int(num+.01)}')
