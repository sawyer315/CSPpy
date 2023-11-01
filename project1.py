#quiz
import random

score = 0
qNum = 1
questions = []
answers = []
randNum = 0
response = 0
difficulty = int(input("Difficulty -> 1 or 2"))
startLen = int(input("How many questions?"))

orderList = range(1, startLen)
randC = 0
randPartA = 0
randPartB = 0

def makeQuestion(diff):
  if diff == 2:
    randC = random.randint(1, 5)
  else:
    randC = random.randint(1, 2)

  randPartA = 0
  randPartB = 0
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


for i in range(0, startLen - 1):
  makeQuestion(difficulty)



def randOrder(*args):
  

  
randOrder(orderList)

while qNum <= startLen:
  
  print("Q", qNum)
  print(questions[qNum - 1])
  response = int(input())
  if response == answers[qNum - 1]:
    score += 2
    print("Correct")
    print("Score: ", score)
  else:
    score -= 1
    print("Incorrect")
    print("Score: ", score)
  qNum += 1 