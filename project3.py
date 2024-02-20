tasks = []
edit = 1
select = 0
editing = ""
string = ""
completed = []

while edit == 1:
  if len(tasks) > 0: print('Current list: ',tasks)
  editing = str(input("Add or remove a task?"))
  if editing == 'add':
    string = str(input('?'))
    tasks.append(string)
  elif editing == 'remove':
    select = int(input("What position? "))
    tasks.pop(select-1)
  elif editing == 'done':
    edit = 0

while edit == 0:
  completed = [False] * len(tasks)
  for i in range(0, len(tasks)):
    print(tasks[i],': ',completed[i])
  editing = str(input("Complete which task?"))
  for i in range(0, len(tasks)):
    if editing == i:
      if completed[i] == False: completed[i] = True

