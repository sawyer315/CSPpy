roman = str(input("?: "))
arabic = 0
for char in roman:
  if char == "I":
    arabic += 1
  elif char == "V":
    arabic += 5
  elif char == "X":
    arabic += 10
  elif char == "L":
    arabic += 50
  elif char == "C":
    arabic += 100
  elif char == "D":
    arabic += 500
  elif char == "M":
    arabic += 1000

print(arabic)