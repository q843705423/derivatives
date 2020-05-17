import numpy as np


def forecast(result_file_path, test_data_x_path, p_data_path):
    file = open(result_file_path, "w+")
    testDataX = np.loadtxt(test_data_x_path)
    P = np.loadtxt(p_data_path)
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
        info = "股票明日收盘价比今日收盘价涨跌{0}%到{1}%的概率约为:{2}%".format(str(i - 10), str(i - 9), str(round(cnt, 3)))
        file.write(info + "\n")
        print(info)
    print("欢迎找我分析股票")
    file.close()
