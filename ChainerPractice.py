# -*- coding: utf-8 -*-
__author__ = 'kawakami_note'

import chainer
import numpy as np
from chainer import cuda, Function, gradient_check, Variable, optimizers, serializers, utils
from chainer import Link, Chain, ChainList
import chainer.functions as F
import chainer.links as L

x_data = np.array([5], dtype=np.float32)
x = Variable(x_data)
y = x**2 - 2 * x + 1
print(x.data)
y.backward()
print(x.grad)

z = 2 * x
y = x**2 - z + 1
y.backward(retain_grad=True)
print(x.data)
print(x.grad)
print(z.grad)

# gradは微分した結果を示す
x = Variable(np.array([[1,2,3],[4,5,6]], dtype=np.float32))
y = x**2 - 2*x + 1
y.grad = np.ones((2,3), dtype=np.float32)
print(y.grad)
y.backward()
print(x.grad)

# 関数は f(x) = 3s + 2 と定義
f = F.Linear(3, 2)
# W:ランダムな値 b:0値
print(f.W.data)
print(f.b.data)

x = Variable(np.array([[1,2,3],[4,5,6]], dtype=np.float32))
y = f(x)
print(y.data)

f.zerograds()

y.grad = np.ones((2,2),dtype=np.float32)
y.backward()
print(f.W.grad)
print(f.b.grad)


class MyChain(Chain):
    def __init__(self):
        super(MyChain, self).__init__(
            l1=L.Linear(4, 3),
            l2=L.Linear(3, 2),
        )

    def __call__(self, x):
        h = self.l1(x)
        return self.l2(h)

class MyChain2(ChainList):
    def __init__(self):
        super(MyChain2, self).__init__(
            L.Linear(4, 3),
            L.Linear(3, 2),
        )

    def __call__(self, x):
        h = self[0](x)
        return self[1](h)

x = Variable(np.array([[1,2,3,4],[5,6,7,8]], dtype=np.float32))
model = MyChain()
optimizer = optimizers.SGD()
optimizer.setup(model)

model.zerograds()
optimizer.update()
