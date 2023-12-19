#Grocery list
grocery = []
ready = 0
name = ""
amount = 0
label = ""
select = 0
count = 0


#def findMost(list):
  

while ready == 0:
  command = str(input("(add, remove, done, sort) "))
  if command == "add":
    name = str(input("Name? "))
    amount = int(input("Amount? "))
    label = name + ", " + str(amount)
    grocery.append(label)
    count += 1
  elif command == "remove":
    select = int(input("What position? "))
    grocery.pop(select-1)
  elif command == "done":
    ready = 1
  elif command == "sort":
    grocery.sort()
  else:
    print("Try again ")
  print(grocery)
