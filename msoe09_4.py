import math

def fun(x):
  return (math.exp(-x * x / 2)) / (math.sqrt(2 * math.pi))

a = int(input("a = "))
b = int(input("b = "))
num = int(input("n = "))
h = (b - a) / num
sum = 0
for i in range(0, num - 1):
  sum += fun(a + (h * i))

print(sum)