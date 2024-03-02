import random
player_move = ''
cpu_move = ''
past_player_moves = []
past_cpu_moves = []
cpu_type = ''
R = 0
T = 0
S = 0
P = 0
game_length = int(input('Length of a game? '))
settings = str(input('Rules: Standard, Cooperative, Uncooperative, Simple, Even? '))
if settings == 'Standard':
  R,T,S,P = 3,5,0,1
elif settings == 'Cooperative':
  R,T,S,P = 4,5,1,0
elif settings == 'Uncooperative':
  R,T,S,P = 3,6,0,2
elif settings == 'Simple':
  R,T,S,P = 2,3,0,1
elif settings == 'Even':
  R,T,S,P = 3,3,1,1
print(R,T,S,P)
turn = 0
temp = 0
player_reward = 0
cpu_reward = 0
player_score = 0
cpu_score = 0

def cpu_decide(type):
  if type == 'Trusting':
    return 'Co'
  elif type == 'Distrustful':
    return 'Be'
  elif type == 'Random':
    temp = random.randint(1,2)
    if temp == 1: return 'Co'
    else: return 'Be'
  elif type == 'Copycat':
    if turn == 1:
      temp = random.randint(1,2)
      if temp == 1: return 'Co'
      else: return 'Be'
    else:
      if player_move[-1] == 'Co': return 'Co'
      else: return 'Be'
  elif type == 'Opposite':
    if turn == 1:
      temp = random.randint(1,2)
      if temp == 1: return 'Co'
      else: return 'Be'
    else:
      if player_move[-1] == 'Co': return 'Be'
      else: return 'Co'
  elif type == 'Alternate':
    if turn == 1:
      temp = random.randint(1,2)
      if temp == 1: return 'Co'
      else: return 'Be'
    else: 
      if cpu_move[-1] == 'Co': return 'Be'
      else: return 'Co'
  elif type == 'Grudge':
    if turn == 1:
      return 'Co'
    else:
      for item in past_player_moves:
        if item == 'Be': return 'Be'
      return 'Co'
  elif type == 'Thinker':
    if turn == 1:
      return 'Co'
    elif turn == 2:
      if past_player_moves[-1] == 'Co': return 'Co'
      else: return 'Be'
    else:
      if past_player_moves[-1] and past_player_moves[-2] == 'Co': return 'Be'
      if past_player_moves[-1] and past_player_moves[-2] == 'Be': return 'Be'
      else: return past_player_moves[-1]
  elif type == 'Generous':
    if turn == 1 or 2:
      return 'Co'
    else:
      if past_player_moves[-1] and past_player_moves[-2] == 'Be': return 'Be'
      else: return 'Co'
  elif type == 'Wary':
    if turn == 1:
      return 'Co'
    else:
      if past_player_moves[-1] or past_player_moves[-2] == 'Be': return 'Be'
      else: return 'Co'
  print(cpu_move)
def calc_rewards(p1, p2):
  if p1 == 'Co' and p2 == 'Co': return R,R
  elif p1 =='Be' and  p2 == 'Be': return P,P
  elif p1 == 'Co' and p2 == 'Be': return S,T
  elif p1 == 'Be' and p2 == 'Co': return T,S
  else: return 0,0
 

temp = random.randint(1,10)
if temp == 1: cpu_type = 'Trusting'
elif temp == 2: cpu_type = 'Distrustful'
elif temp == 3: cpu_type = 'Random'
elif temp == 4: cpu_type = 'Copycat'
elif temp == 5: cpu_type = 'Opposite'
elif temp == 6: cpu_type = 'Alternate'
elif temp == 7: cpu_type = 'Grudge'
elif temp == 8: cpu_type = 'Thinker'
elif temp == 9: cpu_type = 'Generous'
elif temp == 10: cpu_type = 'Wary'
print(cpu_type)
turn = 1
for i in range(game_length):
  print('================================================')
  player_move = str(input('Your move? (Cooperate/Betray) '))
  if player_move == 'Cooperate': player_move = 'Co'
  if player_move == 'Betray': player_move = 'Be'
  cpu_move = cpu_decide(cpu_type)
  if cpu_move == 'Be': print('CPU move: Betray')
  if cpu_move == 'Co': print('CPU move: Cooperate')
  past_player_moves.append(player_move)
  past_cpu_moves.append(cpu_move)
  player_reward, cpu_reward = calc_rewards(player_move, cpu_move)
  player_score += player_reward
  cpu_score += cpu_reward
  if player_reward == R:
    print('Both players rewarded')
  elif player_reward == P:
    print('Both players punished')
  elif player_reward == S:
    print('Player was betrayed')
  elif player_reward == T:
    print('CPU was betrayed')
  print('Current score:')
  print('Player: ', player_score)
  print('CPU score: ', cpu_score)
  turn +=1
print('============================================')
print('GAME OVER')
if player_score>cpu_score: print('You win!')
elif player_score<cpu_score: print('You lose!')
elif player_score == cpu_score: print('Tie!')
print('Final score: ',player_score,', ',cpu_score)