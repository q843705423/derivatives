import numpy as np
# 真正的读取，并且跑参数
dataX = np.loadtxt("D:\\dataX.txt")
dataY = np.loadtxt("D:\\dataY.txt")
# dataX = np.loadtxt("dataX.txt")
# dataY = np.loadtxt("dataY.txt")
dataY = np.array([dataY])
dataY = np.transpose(dataY)
print(dataY)
dataX = np.column_stack((dataX, np.ones(dataX.shape[0])))

rate = 0.1
m, n = dataX.shape
P = np.ones([1, n])
step = 0
while step < 100_0000:
    temp = np.dot(dataX, np.transpose(P)) - dataY
    # print(temp)
    cost = np.dot(np.transpose(dataX), temp)
    m_ = np.transpose(cost * rate) / (2 * m)
    P -= m_
    if step % 10000 == 0:
        [lost] = temp.sum(0)
        print("step:", step, "lost is ", lost)
        print(P)
    step += 1
np.savetxt("D:\\dataZ.txt", P)
