__author__ = 'kawakami_note'

words = ['cat', 'window', 'defenestrate']
for word in words:
    print(word, len(word))

for word in words[:]:
    if len(word) > 6:
        words.insert(0, word)
print(words)

for index in range(4):
    print(words[index])

fiveToTen = range(5, 10)
print(fiveToTen)