numbers = []
for i in range(0, 10):
  numbers.append(float(input(f'Number {i+1}: ')))
  numbers.sort()
  if i >= 2: print(numbers[-3], 'is the third largest number.')
