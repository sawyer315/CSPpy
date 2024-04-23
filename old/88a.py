import math

num1 = int(input("Number 1: "))
num2 = int(input("Number 2: "))

sum = num1 + num2
dif = num1 - num2
product = num1 * num2
avg = sum / 2
abs = abs(dif)
if num1 > num2:
  max = num1
  min = num2
else:
  max = num2
  min = num1

print("Numbers: ", num1, ", ", num2)
print("Sum: ", sum)
print("Difference: ", dif)
print("Product: ", product)
print("Average: ", avg)
print("Absolute value: ", abs)
print("Max: ", max)
print("Min: ", min)