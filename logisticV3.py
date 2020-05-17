import numpy as np
import time


def GeneratingParameters(data_x_file_path, data_y_file_path, data_p_file_path):
    dataX = np.loadtxt(data_x_file_path)
    dataY = np.loadtxt(data_y_file_path)
    dataY = dataY.reshape(-1, 1)
    m, n = dataX.shape
    dataY_M, dataY_N = dataY.shape
    P = np.ones([dataY_N, n + 1])
    e = 2.718281828459
    a = 0.001
    dataY = np.array(dataY)
    dataX = np.column_stack((dataX, np.ones(dataX.shape[0])))
    step = 0
    startTime = time.time()
    while step < 100_0000:
        # print(step, Xthrea)
        Xthrea = np.dot(dataX, np.transpose(P))
        # print(step, Xthrea)
        Xthrea = 1.0 / (1 + e ** (-Xthrea))
        temp = Xthrea - dataY
        # print(temp)
        s = np.transpose(temp).dot(dataX)
        P = P - a / m * s
        step += 1
        if step % 2_0000 == 0:
            j = np.dot(dataX, np.transpose(P)) > 0
            # print(P)
            errNum = np.abs(j - dataY).sum()
            endTime = time.time()
            np.savetxt(data_p_file_path, Xthrea)
            print("step:", step, "准确度:", (m * dataY_N - errNum) / m / dataY_N, "spend time", endTime - startTime)
            startTime = endTime
    print("ok")
# GeneratingParameters("sh603717.day");
