#quiz
import random

score = 0
qNum = 1
questions = []
answers = []
randNum = 0
response = 0
difficulty = int(input("Difficulty -> 1 or 2? "))
startLen = int(input("How many questions? "))
orderList = []
for i in range(1, startLen+1):
  orderList.append(i)
randC = 0
randPartA = 0
randPartB = 0
def makeQuestion(diff):
  if diff == 2:
    randC = random.randint(1, 5)
  else:
    randC = random.randint(1, 2)

  randPartA = 3
  randPartB = 2
  output = ""
  if randC == 1:
    randPartA = random.randint(10, 100)
    randPartB = random.randint(1, 100)
    output = f"{randPartA} + {randPartB} = ?"
    questions.append(output)
    answers.append(randPartA + randPartB)
  elif randC == 2:
    randPartA = random.randint(10, 100)
    randPartB = random.randint(1, randPartA)
    output = f"{randPartA} - {randPartB} = ?"
    questions.append(output)
    answers.append(randPartA - randPartB)
  elif randC == 3:
    randPartA = random.randint(3, 20)
    randPartB = random.randint(2, 20)
    output = f"{randPartA} x {randPartB} = ?"
    questions.append(output)
    answers.append(randPartA * randPartB)
  elif randC == 4:
    while randPartA % randPartB != 0:
      randPartA = random.randint(4, 100)
      randPartB = random.randint(2, 50)
      output = f"{randPartA} / {randPartB} = ?"
    questions.append(output)
    answers.append(randPartA / randPartB)
  else:
    randPartA = random.randint(2, 9)
    randPartB = random.randint(2, 4)
    output = f"{randPartA} ^ {randPartB} = ?"
    questions.append(output)
    answers.append(randPartA ** randPartB)

for i in range(0, startLen):
  makeQuestion(difficulty)

tempList = []
for i in range(0, startLen - 1):
  tempRand = random.randint(0, len(orderList) - 1)
  tempList.append(orderList[tempRand])
  orderList.pop(tempRand)

tempList += orderList
orderList = tempList

streak = 0

for qNum in range(1, startLen + 1):
  print("Q", qNum)
  temp = orderList[qNum - 1]
  print(questions[temp - 1])
  response = int(input())
  if response == answers[temp - 1]:
    streak += 1
    score += 1 + (streak - 1)
    print("Correct")
    print("Score: ", score, "\n")
  else:
    streak = 0
    score -= 1
    print("Incorrect")
    print("Score: ", score, "\n")