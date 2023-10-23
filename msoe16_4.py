from sympy import factorint
num = int(input("Number: "))

factors  = str(factorint(num))

nums = factors.split()
nums_final = []
for item in nums:
  for char in item:
    if char.isdigit():
      nums_final.append(int(char))

print(sum(nums_final))
totient_nums = []
for i in range(0, len(nums_final)//2):
  totient_nums.append((nums_final[i]^(nums_final[i + 1] - 1)) * (nums_final[i] - 1))

print(totient_nums)