#Grocery list
grocery = []
ready = 0
name = ""
amount = 0
label = ""
select = 0
amounts = []
most = 0

targ = 0

def isEqual(num1, num2):
  return num1 == num2
def findMost(list):
  for item in list:
    amounts.append(str(item)[-1])
  amounts.sort()
  return amounts[-1]
def countNumber(list, target):
  answer = 0
  for item in list:
    if isEqual(item, target) is True:
      answer += 1
  return answer
while ready == 0:
  command = str(input("(add, remove, done, sort) "))
  if command == "add":
    name = str(input("Name? "))
    amount = int(input("Amount? "))
    label = name + ", " + str(amount)
    grocery.append(label)
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
for item in grocery:
  print(item)
print("Highest amount: ", findMost(grocery))
targ = input("How many of what amount? ")
print(countNumber(amounts, targ))