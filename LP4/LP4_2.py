weight = int(input("Weight:"))
length = int(input("Length:"))
width = int(input("Width:"))
height = int(input("Height:"))

vol = length * width * height

if weight > 27 and vol > 100000:
  out = "Too heavy and too large."
elif weight > 27:
  out = "Too heavy."
elif vol > 100000:
  out = "Too large."
else:
  out = "Package is good."

print(out)