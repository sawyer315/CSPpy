import re

text = str(input("Searching in?:"))
searchFor = str(input("Looking for? "))
answer = re.findall(searchFor, text)

print(len(answer))