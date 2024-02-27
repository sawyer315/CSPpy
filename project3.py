tasks = []
edit = 1
select = 0
select2 = 0
editing = ""
string = ""
completed = []
temp = ''
def switch(chose):
  if chose == '': return
  for i in range(0, len(tasks)):
    if int(chose) == i+1:
      if completed[i] is False: completed[i] = True
      elif completed[i] is True: completed[i] = False
while edit == 1:
  while edit == 1:
    print("---------------------------------")
    if len(tasks) > 0: 
      for i in range(0, len(tasks)):
        print(i+1, ': ', tasks[i])
    editing = ''
    while editing == '':
      editing=str(input("Add or remove a task? Or: done, sort, quit, change or swap: "))
    if editing == 'add':
      string = str(input('?: '))
      tasks.append(string)
    elif editing == 'remove':
      select = int(input("What position?: "))
      tasks.pop(select-1)
    elif editing == 'done': edit = 0
    elif editing == 'sort': tasks.sort()
    elif editing == 'swap':
      if len(tasks) > 1:
        select = int(input('What position?'))-1
        temp = tasks[select]
        select2 = int(input('Move to where?'))-1
        tasks[select] = tasks[select2]
        tasks[select2] = temp
      else:
        print('Add more tasks.')
    elif editing == 'change' and len(tasks)>0:
      select = int(input('What position?'))-1
      select2 = str(input('To what?'))
      tasks[select] = select2
    elif editing == 'quit': edit = 2
  completed = []
  while edit == 0:
    if completed == []: completed = [False] * len(tasks)
    print("---------------------------------")
    for i in range(0, len(tasks)):
      if completed[i] is True: print(tasks[i],': ','Done')
      if completed[i] is False: print(tasks[i],': ','Not Done')
    editing = ''
    while editing == '':
      editing = str(input("Complete which task? (0 to quit, -1 to edit): "))
    if int(editing) == 0: edit = 2
    elif int(editing) == -1: edit = 1
    else: switch(editing)