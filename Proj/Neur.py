import numpy as np


def sigmoid(x):
    return 1 / (1 + np.exp(-x))


def derivative(x):
    return x*(1 - x)


x = np.array([[0.7, 0.9, 1.0, 2.0],
              [0.3, 1.1, 4.0, 4.5],
              [1.2, 1.1, -3.0, 2.0],
              [0.6, 0.5, 2.5, 2.0],
              [0.1, 0.1, -1.0, 0.0],
              [0.8, 0.2, 1.5, -3.0]])
y = np.array([[1, 0, 0, 1, 1, 0]]).T
syn0 = 2*np.random.random((4, 7)) - 1
syn1 = 2*np.random.random((7, 3)) - 1
syn2 = 2*np.random.random((3, 1)) - 1
for i in range(50000):
    l1 = sigmoid(np.dot(x, syn0))
    l2 = sigmoid(np.dot(l1, syn1))
    l3 = sigmoid(np.dot(l2, syn2))
    l3_delta = (y - l3) * derivative(l3)
    l2_delta = l3_delta.dot(syn2.T) * derivative(l2)
    l1_delta = l2_delta.dot(syn1.T) * derivative(l1)
    syn2 += l2.T.dot(l3_delta)
    syn1 += l1.T.dot(l2_delta)
    syn0 += x.T.dot(l1_delta)
    if (i % 10000) == 0:
        print("Error:" + str(np.mean(np.abs(y - l3))))
