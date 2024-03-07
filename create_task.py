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
  print(cpu_move)
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
  
  print(cpu_type)
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
  print('============================================')
  print('GAME OVER')
  if player_score>cpu_score: print('You win!')
  elif player_score<cpu_score: print('You lose!')
  elif player_score == cpu_score: print('Tie!')
  print('Final score: ',player_score,', ',cpu_score)


elif gamemode == 'Simulate':
  p1_type = 0
  p2_type = 1
  type1_score,type2_score,type3_score,type4_score,type5_score,type6_score,type7_score,type8_score,type9_score,type10_score = 0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0
  

  for i in range(100):
    p1_type +=1
    if p1_type == 11:
      p1_type = 1
      p2_type+=1
   
      
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
    print('============================================')
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
  print('Trusting: ', type1_score)
  print('Distrusting: ', type2_score)
  print('Random: ', type3_score)
  print('Copycat:', type4_score)
  print('Opposite: ', type5_score)
  print('Alternate:', type6_score)
  print('Grudge:', type7_score)
  print('Thinker: ', type8_score)
  print('Generous: ', type9_score)
  print('Wary: ', type10_score)