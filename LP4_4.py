model = int(input("Model number: "))

if model == 119 or model == 179 or model == 221 or model == 780 or 189 <= model <= 195:
  defect = True
else:
  defect = False

if defect == True:
  print("Your car is defective, it must be repaired.")

if defect == False:
  print("Your car is not defective.")

