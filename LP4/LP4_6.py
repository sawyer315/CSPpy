import random

num1 = random.randint(1, 10)
num2 = random.randint(1, 10)
opp = random.randint(1, 4)

if opp == 1:
  sign = "+"
  ans = num1 + num2
elif opp == 2:
  sign = "-"
  ans = num1 - num2
elif opp == 3:
  sign = "*"
  ans = num1 * num2
else:
  sign = "/"
  ans = num1 / num2
  ans = round(ans, 1)

print("What is ", num1, sign, num2, "?")
input = float(input())
input = round(input, 1)

if input == ans:
  print("Correct")
else:
  print("Incorrect, the answer was: ", ans)

