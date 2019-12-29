import numpy as np

# 手动实现回归
#

dataX = [
    [3, 1, 1],
    [4, 3, 1],
    [6, 5, 1],
    [0, 0, 1],
]
dataY = [
    [4],
    [10],
    [16],
    [1],
]
dataX = np.array(dataX)
m, n = dataX.shape
# 学习速率
rate = 0.1
# p = np.random.normal(1, 2, [1, 3])
# p = np.ones((1, 3)) // [[1, -1, 0]]
p = np.ones([1, 3])
step = 0
while step < 10000:
    temp = np.dot(dataX, np.transpose(p)) - dataY
    cost = np.dot(np.transpose(dataX), temp)
    m_ = np.transpose(cost * rate) / (2 * m)
    p -= m_
    print(p)
    step += 1
