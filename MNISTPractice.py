# -*- coding: utf-8 -*-
__author__ = 'kawakami_note'

import numpy as np
from sklearn.datasets import fetch_mldata
from chainer import Chain
import chainer.links as L
import chainer.functions as F
from chainer import optimizer, optimizers
from chainer import Variable

mnist = fetch_mldata('MNIST original')

x_all = mnist['data'].astype(np.float32) / 255
y_all = mnist['target'].astype(np.int32)
x_train, x_test = np.split(x_all, [60000])
y_train, y_test = np.split(y_all, [60000])

class MLP(Chain):
    def __init__(self):
        super(MLP, self).__init__(
            l1=L.Linear(784, 100),
            l2=L.Linear(100, 100),
            l3=L.Linear(100, 10)
        )

    def __call__(self, x):
        h1 = F.relu(self.l1(x))
        h2 = F.relu(self.l2(h1))
        y = self.l3(h2)
        return y

class Classifier(Chain):
    def __init__(self, predictor):
        super(Classifier, self).__init__(predictor=predictor)

    def __call__(self, x, t):
        y = self.predictor(x)
        self.loss = F.softmax_corss_entropy(y, t)
        self.accuracy = F.accuracy(y, t)
        return self.loss

model = L.Classifier(MLP())
optimizer = optimizers.SGD()
optimizer.setup(model)

batch_size = 100
data_size = 60000
for epoch in range(20):
    print('epoch %d' % epoch)
    indexes = np.random.permutation(data_size)
    for index in range(0, data_size, batch_size):
        x = Variable(x_train[indexes[index : index + batch_size]])
        t = Variable(y_train[indexes[index : index + batch_size]])
        optimizer.update(model, x, t)

sum_loss, sum_accuracy = 0, 0
for index in range(0, 10000, batch_size):
    x = Variable(x_test[index : index + batch_size])
    t = Variable(y_test[index : index + batch_size])
    loss = model(x, t)
    sum_loss += loss.data * batch_size
    sum_accuracy += model.accuracy.data * batch_size

main_loss = sum_loss / 10000
main_accuracy = sum_accuracy / 10000
print(main_loss)
print(main_accuracy)