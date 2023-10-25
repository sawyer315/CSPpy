import random
import math

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
#11
temp = []
for i in range(0, 20):
  if int(bigArray[i]) % 4 == 0:
    temp.append(bigArray[i])
print("Multiples of 4: ", temp)
temp = 0
for i in range(0, 20):
  if bigArray[i] == 60:
    temp = 1

if temp == 1:
  print("There is a 60 in the list.")
else:
  print("There is not a 60 in the list")

reverseArray = []

for i in range(0, 20):
  reverseArray.insert(0, bigArray[i])

print(reverseArray)

if reverseArray == bigArray:
  print("Palindromic")
else:
  print("Not palindromic")
#14
totAvg = 0
temp = []
for i in range(0, 20):
  totAvg += bigArray[i]
totAvg /= 21
print("Average ", totAvg)
for i in range(0, 20):
  if bigArray[i] > totAvg:
    temp.append(bigArray[i])

print("Larger than average: ", temp)

#15
temp = []
for i in range(0, 20):
  if bigArray[i] % 2 == 0:
    temp.append(bigArray[i])

print("Even: ", temp)

#16
print("Reverse order: ", reverseArray)

#18
sum = 0
for i in range(0, 20):
  sum += bigArray[i]
print("Sum: ", sum)

#17

las = bigArray[19]
temp = list(bigArray)
temp.pop(19)
temp.insert(0, las)

print("Original: ", bigArray)
print("\nShifted: ", temp)