import random
bigArray = []
for i in range(0, 19):
  bigArray.append(random.randint(20, 90))

print(bigArray)

for i in range(0, 19):
  print(bigArray[i])

fir = bigArray[0]
las = bigArray[18]
mid = bigArray[9]
print("Middle number is: ", mid)
avg = (fir + mid + las)/3
print("Average of first, middle, and last numbers is: ", avg)

small = 91
big = 19
for i in range(0, 19):
  if bigArray[i] > big:
    big = bigArray[i]
  if bigArray[i] < small:
    small = bigArray[i]

print("Biggest: ", big, " Smallest: ", small)

bigArray.remove(las)
bigArray.insert(0, las)

bigArray.remove(fir)
bigArray.insert(19, fir)

print(bigArray, "\n")
bigArray.insert(9, random.randint(1, 10))
print(bigArray, "\n")
for i in range(0, 20):
  bigArray[i] += 10
print(bigArray)

thr = bigArray[2]
print("Out: ", thr)
bigArray.insert(2, 5)
bigArray.remove(thr)

print(bigArray, "\n")
temp = []
for i in range(0, 20):
  if 50 <= bigArray[i] and bigArray[i] <= 59:
    temp.append(bigArray[i])
print("50's: ", temp)

for i in range(0, 20):
  if bigArray[i] % 4 == 0:
    temp.append(bigArray[i])
print("Multiples of 4: ", temp)