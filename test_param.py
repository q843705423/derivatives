import numpy as np

# 加载验证数据集合
testDataX = np.loadtxt("D:\dataXTest.txt")
testDataY = np.loadtxt("D:\dataYTest.txt")
p = np.loadtxt("D:\\dataZ.txt")

# 右边添加一列为 1
testDataX = np.column_stack((testDataX, np.ones(testDataX.shape[0])))

testDataY = np.array([testDataY])
p = np.array([p])
print(testDataX.shape)
print(testDataY.shape)
print(p.shape)
# res = np.dot(testDataX, testDataY)
# np.transpose(testDataX).dot()
res = np.dot(testDataX, np.transpose(p))
print(res.shape)
allCost = res - np.transpose(testDataY)
# 低于预期超过4%的概率为 48/2800 = 24/1400 = 12/700 = 12/500 = 24/1000 = 2.4%不到
# 低于预期超过3%的概率为 87/2800 = 24/1400 = 12/700 = 12/500 = 24/1000 = 2.4%不到
# 低于预期超过2%的概率为 87/2800 = 24/1400 = 12/700 = 12/500 = 24/1000 = 2.4%不到
# 低于预期的概率为 1481/2800 = 24/1400 = 12/700 = 12/500 = 24/1000 = 2.4%不到
# lossSum = 0
lossRange = [-500, -400, -300, -200, -100, 0, 100, 200, 300, 400, 500]
lossSum = [0] * len(lossRange)
for i in range(0, 2800):
    loss = (testDataY[0][i] - res[i][0]) / testDataY[0][i] * 10000
    for j in range(0, 7):
        if lossRange[j] < loss < lossRange[j + 1]:
            lossSum[j] += 1

for i in range(0, len(lossRange) - 1):
    print(lossRange[i], lossRange[i + 1], lossSum[i])
# print(res[1][0])

# 得出结论，该拟合曲线能够让 预测股价与实际估计的差距控制在-5%到2%之间
