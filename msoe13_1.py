r1 = int(input("R1: "))
r2 = int(input("R2: "))
r3 = int(input("R3: "))
V = int(input("V: "))

i1 = V/r1
i2 = V/r2
i3 = V/r3

sum = i1 + i2 + i3

total = V/sum

print("Ohms: ", total)