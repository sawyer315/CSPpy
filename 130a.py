num = int(input("n = ? "))
if num == 1:
  print("???")
old = 0
steps = 0
while num != 1:
  steps += 1
  if num % 2 == 0:
    old = num
    num /= 2
    print(old," is even, so I take half: ", num)
  else:
    old = num
    num = (num * 3) + 1
    print(old, " is odd, so 3n+1: ", num)

print("Stpes = ", steps)