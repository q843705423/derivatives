import numpy as np
import pymysql
import logisticV3


def getData():
    return np.loadtxt('C:/Users/Administrator/Desktop/111.txt')


def readDataFromDatabase(code="sh513050"):
    conn = pymysql.connect(host='127.0.0.1', user='root', password='root', database='stock_project', charset='utf8')
    cursor = conn.cursor()
    sql = "select * from stock_transaction_info where code = '" + code + "';"
    cursor.execute(sql)
    result = cursor.fetchall()
    # value = ret['name']
    cursor.close()
    conn.close()
    return result


def calculateCCI(data, P):
    OPEN = 0
    HIGH = 1
    LOW = 2
    CLOSE = 3
    # data = getData()
    typePrice = (data[:, LOW] + data[:, CLOSE] + data[:, HIGH]) / 3.0
    len_typePrice = len(typePrice)
    MAArr = []
    MDArr = []
    for i in range(P - 1):
        MAArr.append(0.0)
    for i in range(P - 1, len_typePrice):
        sum_of_type_price = sum(typePrice[i - P + 1: i + 1] / P)
        MAArr.append(np.round(sum_of_type_price, 2))
    for i in range(P - 1):
        MDArr.append(0.001)
    for i in range(P - 1, len_typePrice):
        np_abs = np.abs(np.array(typePrice[i - P + 1:i + 1] - MAArr[i]))
        np_res = np.round(np_abs, 2)
        MDValue = np.sum(np_res) / P
        MDArr.append(MDValue)
    CCI = (typePrice - MAArr) / (np.array(MDArr) * 0.015)
    return CCI


if __name__ == '__main__':
    data = readDataFromDatabase("sh600007")
    # print(data)
    # print(len(data))
    dateList = [i[8] for i in data]
    openValue = [i[2] for i in data]
    closeValue = [i[3] for i in data]
    highValue = [i[4] for i in data]
    lowValue = [i[5] for i in data]
    d = [openValue, closeValue, highValue, lowValue]
    data = np.transpose(np.array(d))
    print(data.shape)
    cciList = calculateCCI(data, 14)
    cciList_len = len(cciList)
    rate = []
    P = 14
    arr = []
    for i in range(P + 1, cciList_len - 14):
        for j in range(0, 14):
            arr.append(cciList[i + j])
    reshape = np.array(arr).reshape((-1, 14))
    # reshape = np.transpose(reshape)
    reshape = reshape / 100.0
    np.savetxt("D:/cqqX.txt", reshape)
    # 1950 #1908 42
    ansArr = []
    for i in range(P + 14, cciList_len - 1):

        if (closeValue[i + 1] - closeValue[i]) / closeValue[i] * 100 >= 1:
            ansArr.append(1)
            # ansArr.append(0)
            # ansArr.append(0)
        else:
            ansArr.append(0)
            # ansArr.append(1)
            # ansArr.append(0)
    np.savetxt("D:/cqqY.txt", (np.array(ansArr).reshape(-1, 1)))

    logisticV3.GeneratingParameters("D:/cqqX.txt", "D:/cqqY.txt", "D:/cqqP.txt")

    pass
    # calculateCCI(20)
