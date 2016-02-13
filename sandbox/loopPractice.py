__author__ = 'kawakami_note'

import numpy as np

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
print(list(fiveToTen))

array = ['Mary', 'had', 'a', 'little', 'lamb']
for index in range(len(array)):
    print(index, array[index])

def loopTest():
    for index in range(5, 10):
        for count in range(4):
            if index == 7:
                break
            print(index, count)

def np_practice():
    randoms = np.random.randint(25, 50, (10, 2))
    centers = np.random.randint(25, 50, (10, 2))
    print(randoms)
    print(centers)
    for random in randoms:
        min_dimension = -1
        index = 0
        min_index = 0
        for center in centers:
            dimension = np.sqrt(np.add(np.power(random[0] - center[0], 2), np.power(random[1] - center[1], 2)))
            if min_dimension == -1 or min_dimension > dimension:
                min_dimension = dimension
                min_index = index
            index += 1
        print(str(min_index), str(min_dimension))


np_practice()
