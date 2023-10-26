from sympy import factorint
num = int(input("Number: "))

factors  = str(factorint(num))

nums = factors.split()
nums_final = []
for item in nums:
  for char in item:
    if char.isdigit():
      nums_final.append(int(char))

print(nums_final)
nums_final.append([0]*6)

if len(nums_final) > 1:
  num1 = (nums_final[0] ** (nums_final[1] - 1)) * (nums_final[0] - 1)
  print(num1, " ")
  final = num1
  if len(nums_final) > 3:
    num2 = (nums_final[2] ** (nums_final[3] - 1)) * (nums_final[2] - 1)
    print(num2, " ")
    final *= num2
    if len(nums_final) > 5:
      num3 = (nums_final[4] ** (nums_final[5] - 1)) * (nums_final[4] - 1)
      print(num3, " ")
      final *= num3
      if len(nums_final) > 7:
        num4 = (nums_final[6] ** (nums_final[7] - 1)) * (nums_final[6] - 1)
        print(num4, " ")
        final *= num4

print("Answer: ", final)