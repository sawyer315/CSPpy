per = int(input("Input percentage: "))

if 90 <= per <= 100:
  grade = "A"
elif 80 <= per <= 89:
  grade = "B"
elif 70 <= per <= 79:
  grade = "C"
elif 60 <= per <= 69:
  grade = "D"
else:
  grade = "F"

print("Your grade is: ", grade)
