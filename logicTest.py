import numpy as np


def forecast(code):
    file = open("D:/newstock/" + code + "_result.txt", "w+")
    testDataX = np.loadtxt("D:/newstock/" + code + "_logicZ.txt")
    P = np.loadtxt("D:/newstock/" + code + "_param.txt")
    testDataX = np.column_stack(([testDataX], [[1]]))
    P = np.array(P)
    res = np.dot(P, np.transpose(testDataX))
    e = 2.718281828459
    res_ = 1 / (1 + e ** -res)
    rateForManyProblem = res_.sum(1)
    all_rate = 0
    print(rateForManyProblem.shape)
    for i in range(0, 20):
        all_rate += rateForManyProblem[i]
    for i in range(0, 20):
        values = (rateForManyProblem[i] * 100)
        cnt = values / all_rate
        info = "股票" + code + "明日收盘价比今日收盘价涨跌" + str(i - 10) + "%到" + str(i - 9) + "%的概率约为" + str(round(cnt, 3)) + "%"
        file.write(info + "\n")
        print(info)
    print("欢迎找我分析股票")
    file.close()


