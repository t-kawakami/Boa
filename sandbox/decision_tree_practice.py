__author__ = 'kawakami_note'

import numpy as np
import pandas as pd
from sklearn import tree

data = pd.read_csv('data/wakati.csv')
x_train, x_test = np.split(data['text'], 200)
y_train, y_test = np.split(data['class'], 200)

print(x_train)
print(x_test)
print(y_train)
print(y_test)

classifier = tree.DecisionTreeClassifier()
classifier = classifier.fit(data['text'], data['class'])