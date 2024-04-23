name1 = "Sam Lilly"
name2 = "Fred Biggie"
name3 = "Sally Awesome"
grades = []
with open("prog505b.txt", "r") as f:
  for line in f:
    if line.isnumeric() is True:
      grades.append(int(line))
print(grades)
grade1 = []
grade2 = []
grade3 = []
for i in range(0, 14):
  if i <= 4:
    grade1.append(grades[i])
  elif i <= 9:
    grade2.append(grades[i])
  else:
    grade3.append(grades[i])

print(grade1, grade3)