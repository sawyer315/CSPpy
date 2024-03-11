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
single_player = 0
sets = 0
temp_sum = 0.0
gamemode = input('Gamemode? ')
def cpu_decide(type, self, other):
  if type == 1:
    return 'Co'  #Trusting
  elif type == 2:
    return 'Be'#Distrustful
  elif type == 3:
    temp = random.randint(1,3)
    if temp == 1: return 'Co'
    elif temp == 2: return 'Be'
    else: return 'Ct'#Random
  elif type == 4:
    if turn == 1:
      temp = random.randint(1,3)
      if temp == 1: return 'Co'
      elif temp == 2: return 'Be'
      else: return 'Ct'
    else:
      return other[-1]#Copycat
  elif type == 5:
    if turn == 1:
      temp = random.randint(1,3)
      if temp == 1: return 'Co'
      elif temp == 2: return 'Be'
      else: return 'Ct'
    else:
      if other[-1] == 'Co': return 'Be'
      elif other[-1] == 'Be': return 'Ct'
      else: return 'Co'#Opposite
  elif type == 6:
    if turn == 1:
      temp = random.randint(1,3)
      if temp == 1: return 'Co'
      elif temp == 2: return 'Be'
      else: return 'Ct'
    else: 
      if self[-1] == 'Co': return 'Be'
      elif self[-1] == 'Ct': return 'Co'
      else: return 'Ct'#Alternate#Alternate
  elif type == 7:
    if turn == 1:
      return 'Co'
    else:
      temp = 0
      for item in other:
        if item == 'Be': temp +=1
        temp += 1
      if temp/(turn-1) == 1:
        return 'Co'
      if temp/(turn-1) == 2:
        return 'Ct'
      else: 
        temp = random.randint(1,2)
        if temp == 1: return 'Be'
        else: return 'Ct'#Grudge#Grudge
  elif type == 8:
    if turn == 1:
      return 'Co'
    elif turn == 2:
      if other[-1] == 'Co': return 'Be'
      else: return 'Ct'
    else:
      if other[-1] == 'Co' and other[-2] == 'Co': return 'Be'
      elif other[-1] == 'Be' and other[-2] == 'Be': return 'Ct'
      elif other[-1] == 'Ct': return 'Co'
      else: return other[-1]#Thinker
  elif type == 9:
    if turn == 1 or turn == 2:
      return 'Co'
    else:
      if other[-1] == 'Be' and other[-2] == 'Be': return 'Ct'
      else: return 'Co'#Generous
  elif type == 10:
    if turn == 1 or turn == 2:
      return 'Co'
    else:
      if other[-1] == 'Be' or other[-2] == 'Be': return 'Ct'
      else: return 'Be'#Wary
def calc_rewards(p1, p2):
  if p1 == 'Co' and p2 == 'Co': return R,R
  elif p1 =='Be' and  p2 == 'Be': return P,P
  elif p1 == 'Co' and p2 == 'Be': return S,T
  elif p1 == 'Be' and p2 == 'Co': return T,S
  elif p1 == 'Co' and p2 == 'Ct': return R,S
  elif p1 == 'Ct' and p2 == 'Co': return S,R
  elif p1 == 'Be' and p2 == 'Ct': return S,T
  elif p1 == 'Ct' and p2 == 'Be': return T,S
  elif p1 == 'Ct' and p2 == 'Ct': return P,P
  else: return 0,0
if gamemode == 'Single':
  temp = random.randint(1,10)
  cpu_type = temp
  turn = 1
  for i in range(game_length):
    print('================================================')
    player_move = str(input('Your move? (Cooperate/Betray/Counter) '))
    if player_move == 'Cooperate': player_move = 'Co'
    if player_move == 'Betray': player_move = 'Be'
    if player_move == 'Counter': player_move = 'Ct'
    cpu_move = cpu_decide(cpu_type, past_cpu_moves, past_player_moves)
    print(cpu_move)
    if cpu_move == 'Be': print('CPU move: Betray')
    elif cpu_move == 'Co': print('CPU move: Cooperate')
    elif cpu_move == 'Ct': print('CPU move: Counter')
    past_player_moves.append(player_move)
    past_cpu_moves.append(cpu_move)
    player_reward, cpu_reward = calc_rewards(player_move, cpu_move)
    player_score += player_reward
    cpu_score += cpu_reward
    if player_reward == R:
      print('You were rewarded')
    elif player_reward == P:
      print('You were punished')
    elif player_reward == S:
      print('You lost')
    elif player_reward == T:
      print('You win')
    if cpu_reward == R:
      print('CPU was rewarded')
    elif cpu_reward == P:
      print('CPU was punished')
    elif cpu_reward == S:
      print('CPU lost')
    elif cpu_reward == T:
      print('CPU wins')
    print('Current score:')
    print('Player: ', player_score)
    print('CPU score: ', cpu_score)
    turn +=1
  print('================================================')
  print('GAME OVER')
  if player_score>cpu_score: print('You win!')
  elif player_score<cpu_score: print('You lose!')
  elif player_score == cpu_score: print('Tie!')
  print('Final score: ',player_score,', ',cpu_score)
  print('CPU type: ', cpu_type)

elif gamemode == 'Simulate':
  p1_type = 0
  p2_type = 1
  sets = int(input('How many sets of 100 games? '))
  type1_score,type2_score,type3_score,type4_score,type5_score,type6_score,type7_score,type8_score,type9_score,type10_score = 0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0
  type1_set,type2_set,type3_set,type4_set,type5_set,type6_set,type7_set,type8_set,type9_set,type10_set = [],[],[],[],[],[],[],[],[],[]

  for i in range(sets):
    for i in range(100):
      p1_type +=1
      if p1_type == 11:
        p1_type = 1
        p2_type+=1
      past_player_moves, past_cpu_moves = [],[]
      turn = 1
      for i in range(game_length):
        print('================================================')
        player_move = cpu_decide(p1_type,past_player_moves,past_cpu_moves)
        cpu_move = cpu_decide(p2_type,past_cpu_moves,past_player_moves)
        past_player_moves.append(player_move)
        past_cpu_moves.append(cpu_move)
        player_reward, cpu_reward = calc_rewards(player_move, cpu_move)
        player_score += player_reward
        cpu_score += cpu_reward
        print(player_reward,' ',cpu_reward,' ',player_move,' ',cpu_move)
        print('Player: ', player_score)
        print('CPU score: ', cpu_score)
        turn +=1
      print('================================================')
      print('GAME OVER')
      print('p1: ', p1_type, ', p2 ', p2_type)
      if player_score>cpu_score:
        if p1_type == 1: type1_score +=1
        elif p1_type == 2: type2_score +=1
        elif p1_type == 3: type3_score +=1
        elif p1_type == 4: type4_score +=1
        elif p1_type == 5: type5_score +=1
        elif p1_type == 6: type6_score +=1
        elif p1_type == 7: type7_score +=1
        elif p1_type == 8: type8_score +=1
        elif p1_type == 9: type9_score +=1
        elif p1_type == 10: type10_score +=1
      elif cpu_score>player_score:
        if p2_type  ==  1: type1_score +=1
        elif p2_type == 2: type2_score +=1
        elif p2_type == 3: type3_score +=1
        elif p2_type == 4: type4_score +=1
        elif p2_type == 5: type5_score +=1
        elif p2_type == 6: type6_score +=1
        elif p2_type == 7: type7_score +=1
        elif p2_type == 8: type8_score +=1
        elif p2_type == 9: type9_score +=1
        elif p2_type ==10:type10_score +=1
      else: 
        if p1_type == 1: type1_score +=0.5
        elif p1_type == 2: type2_score +=.5
        elif p1_type == 3: type3_score +=.5
        elif p1_type == 4: type4_score +=.5
        elif p1_type == 5: type5_score +=.5
        elif p1_type == 6: type6_score +=.5
        elif p1_type == 7: type7_score +=.5
        elif p1_type == 8: type8_score +=.5
        elif p1_type == 9: type9_score +=.5
        elif p1_type == 10: type10_score +=.5
        if p2_type  ==  1: type1_score +=.5
        elif p2_type == 2: type2_score +=.5
        elif p2_type == 3: type3_score +=.5
        elif p2_type == 4: type4_score +=.5
        elif p2_type == 5: type5_score +=.5
        elif p2_type == 6: type6_score +=.5
        elif p2_type == 7: type7_score +=.5
        elif p2_type == 8: type8_score +=.5
        elif p2_type == 9: type9_score +=.5
        elif p2_type ==10:type10_score +=.5
      player_score = 0
      cpu_score = 0
    
    type1_set.append(type1_score)
    type2_set.append(type2_score)
    type3_set.append(type3_score)
    type4_set.append(type4_score)
    type5_set.append(type5_score)
    type6_set.append(type6_score)
    type7_set.append(type7_score)
    type8_set.append(type8_score)
    type9_set.append(type9_score)
    type10_set.append(type10_score)
    type1_score,type2_score,type3_score,type4_score,type5_score,type6_score,type7_score,type8_score,type9_score,type10_score = 0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0
    p1_type, p2_type = 0,1
  print(" ")
  for item in type1_set:
    temp_sum += item
  temp_sum = temp_sum / sets
  print('Trusting Avg. ', temp_sum)
  temp_sum = 0
  
  for item in type2_set:
    temp_sum += item
  temp_sum = temp_sum / sets
  print('Distrusting Avg. ', temp_sum)
  temp_sum = 0
  
  for item in type3_set:
    temp_sum += item
  temp_sum = temp_sum / sets
  print('Random Avg. ', temp_sum)
  temp_sum = 0

  for item in type4_set:
    temp_sum += item
  temp_sum = temp_sum / sets
  print('Copycat Avg. ', temp_sum)
  temp_sum = 0

  for item in type5_set:
    temp_sum += item
  temp_sum = temp_sum / sets
  print('Opposite Avg. ', temp_sum)
  temp_sum = 0

  for item in type6_set:
    temp_sum += item
  temp_sum = temp_sum / sets
  print('Alternate Avg. ', temp_sum)
  temp_sum = 0

  for item in type7_set:
    temp_sum += item
  temp_sum = temp_sum / sets
  print('Grudge Avg. ', temp_sum)
  temp_sum = 0

  for item in type8_set:
    temp_sum += item
  temp_sum = temp_sum / sets
  print('Thinker Avg. ', temp_sum)
  temp_sum = 0

  for item in type9_set:
    temp_sum += item
  temp_sum = temp_sum / sets
  print('Generous Avg. ', temp_sum)
  temp_sum = 0

  for item in type10_set:
    temp_sum += item
  temp_sum = temp_sum / sets
  print('Wary Avg. ', temp_sum)
  print('')
  print('Scoring: ', R, ', ', T, ', ', S, ', ', P)
  print('Game length: ', game_length)
  print('Sets of 100 games: ', sets)