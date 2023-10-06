msg = input("Enter Message ")
enc = ""
for let in msg:
  enc += str(ord(let)) + " "
print(enc)
enc2 = ""
for let in enc2:
  enc2 += ascii(ord(let) + 5)
print(enc2)
