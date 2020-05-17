import numpy as np
import time


def GeneratingParameters(code):
    try:
        dataX = np.loadtxt("D:/newstock/" + code + "_logicX.txt")
        dataY = np.loadtxt("D:/newstock/" + code + "_logicY.txt")
        m, n = dataX.shape
        dataY_M, dataY_N = dataY.shape
        P = np.ones([dataY_N, n + 1])
        e = 2.718281828459
        a = 0.01
        dataY = np.array(dataY)
        print("hello world")
        # dataY = np.transpose(dataY)
        dataX = np.column_stack((dataX, np.ones(dataX.shape[0])))
        step = 0
        startTime = time.time()
        while step < 4_0000:
            Xthrea = np.dot(dataX, np.transpose(P))
            Xthrea = 1.0 / (1 + e ** (-Xthrea))
            temp = Xthrea - dataY
            # print(temp)
            s = np.transpose(temp).dot(dataX)
            P = P - a / m * s
            step += 1
            if step % 5000 == 0:
                j = np.dot(dataX, np.transpose(P)) > 0
                # print(P)
                errNum = np.abs(j - dataY).sum()
                endTime = time.time()
                np.savetxt("D:\\newstock/" + code + "_param.txt", P)
                print("step:", step, "准确度:", (m * dataY_N - errNum) / m / dataY_N, "spend time", endTime - startTime)
                startTime = endTime
        print("ok")
    except:
        pass
# GeneratingParameters("sh603717.day");
# GeneratingParameters("sz000739.day");
# GeneratingParameters("sz002095");
