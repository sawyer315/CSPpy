num = int(input('Partition what number? '))
sum = 0
tri = 0
count = 1
parts = []
for i in range(0, 3):
  tri = 0
  count = 1
  if tri + count + sum > num:
    parts.append(0)
  else:
    while tri + count + sum <= num:
      tri += count
      count += 1
    sum += tri
    parts.append(tri)
print(parts)
