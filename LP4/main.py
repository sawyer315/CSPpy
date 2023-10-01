copy = int(input("How many copies?"))
rate = 0.0
if 0 <= copy < 100:
  rate = 0.3
if 100 <= copy < 500:
  rate = 0.28
if 500 <= copy < 750:
  rate = 0.27
if 750 <= copy <= 1000:
  rate = 0.26
if copy > 1000:
  rate = 0.25
total = copy * rate
total = round(total, 2)
print("Price per copy: $", rate)
print("Total cost: $", total)