#Grocery list

grocery = {}
ready = 0
name = ""
amount = 0
rate = 0.0
price = 0.0
label = ""
total = 0.0
select = 0
count = 0

def calc(a, r, n):
  pr = round((a * r), 2)
  la = str(a) + " of " + n
  return pr, la
while ready == 0:
  command = str(input("(add, remove, done) "))
  if command == "add":
    name = str(input("Name? "))
    amount = int(input("Amount? "))
    rate = float(input("Price of one? "))
    price, label = calc(amount, rate, name)
    grocery.update({label:price})
    total += price
    count += 1
  elif command == "remove":
    select = str(input("What item on the list? (Amount + name) "))
    grocery.pop(select)
  elif command == "done":
    ready = 1
  else:
    print("Try again ")
  print(grocery)
print("Total cost: $", total)
print("Avergage cost: $", total/count)
