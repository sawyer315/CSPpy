Text = str(input("Text: "))
words = Text.split()
newWords = []
for i in range(len(words) - 1, -1, -1):
  newWords.append(words[i])
newText = " ".join(newWords)
print(newText)