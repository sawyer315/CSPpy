books = []
with open("prog505a.txt", "r") as f:
  for line in f:
    books.append(int(line[-2]))

points = []
for item in books:
  if item <= 3:
    points.append(item * 10)
  elif item <= 6:
    points.append(30 + ((item - 3) * 15))
  else:
    points.append(75 + ((item - 6) * 20))
i = 0
with open("prog505a.txt", "r+") as file:
  for line in file:
    line += ((" " + str(points[i])))
    i += 1

sum = 0
print(points)
for i in range(0, 5):
  sum += points[i]
avg = sum/5
print("Average points: ", avg)

big = points[0]
for item in points:
  if item > big:
    big = item
