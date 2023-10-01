eggs = int(input("How many eggs?"))
dozen = eggs // 12
eggs = eggs % 12

if 0 <= dozen < 4:
  rate = .5
elif 4 <= dozen < 6:
  rate = .45
elif 6 <= dozen < 11:
  rate = .4
else:
  rate = .35

cost = (dozen * rate) + ((rate / 12) * eggs)
cost = round(cost, 2)
print("The bill is: $", cost)