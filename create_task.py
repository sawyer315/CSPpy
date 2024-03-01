import random
player_move = ''
cpu_move = ''
past_player_moves = []
past_cpu_moves = []
cpu_type = ''
game_length = int(input('Length of a game? '))
turn = 0
temp = 0

def cpu_decide(type):
  if type == 'a':
    return 'Co'
  elif type == 'b':
    return 'Be'
  elif type == 'c':
    temp = random.randint(1,2)
    if temp == 1: return 'Co'
    else: return 'Be'
  elif type == 'd':
    if turn == 1:
      temp = random.randint(1,2)
      if temp == 1: return 'Co'
      else: return 'Be'
    else:
      if player_move[-1] == 'Co': return 'Co'
      else: return 'Be'
  elif type == 'e':
    if turn == 1:
      temp = random.randint(1,2)
      if temp == 1: return 'Co'
      else: return 'Be'
    else:
      if player_move[-1] == 'Co': return 'Be'
      else: return 'Co'
  elif type == 'f':
    if turn == 1:
      temp = random.randint(1,2)
      if temp == 1: return 'Co'
      else: return 'Be'
    else: 
      if cpu_move[-1] == 'Co': return 'Be'
      else: return 'Co'
temp = random.randint(1,4)
if temp == 1: cpu_type = 'a'
elif temp == 2: cpu_type = 'b'
elif temp == 3: cpu_type = 'c'
elif temp == 4: cpu_type = 'd'
elif temp == 5: cpu_type = 'e'
elif temp == 6: cpu_type = 'f' 

turn = 0
for i in range(0,game_length):
  player_move = str(input())
  cpu_move = cpu_decide(cpu_type)

  turn +=1