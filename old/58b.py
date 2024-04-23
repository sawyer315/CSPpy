import math

A = int(input("A: "))
B = int(input("B: "))
C = int(input("B: "))

root1 = ((-1 * B) + (math.sqrt((B ** 2) - (4 * A * C)))) / (2 * A)
root2 = ((-1 * B) - (math.sqrt((B ** 2) - (4 * A * C)))) / (2 * A)

print("")
print("First root: ", root1)
print("Second root: ", root2)