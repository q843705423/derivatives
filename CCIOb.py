import numpy as np
import pymysql
import logisticV3


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


P = 14


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


def anliaze(closeValue, cciList, code):
    len_cciList = len(cciList)
    tdtime = []
    for i in range(len_cciList):
        tdtime.append(0)
    print(cciList)

    time = 0
    for i in range(P + 1, len_cciList):
        if cciList[i] > -20:
            tdtime[i] = 0
        elif cciList[i - 1] < -100 < cciList[i]:
            tdtime[i] = tdtime[i - 1] + 1
        else:
            tdtime[i] = tdtime[i - 1]
        pass

    count = 0
    successCount = 0
    for i in range(P + 1, len_cciList - 1):
        if cciList[i - 1] < -100 < cciList[i] and closeValue[i - 1] > closeValue[i] and tdtime[i] >= 3:
            count += 1
            isSuccess = 0
            for j in range(1, 6):
                if dateList[i] == 20180704:
                    a = 1 + 1
                if closeValue[i + j] > closeValue[i]:
                    isSuccess = 1
            successCount += isSuccess
            if isSuccess == 0:
                print(code, tdtime[i], dateList[i])

    print(count)
    print(successCount)


if __name__ == '__main__':
    code = "sz200028"
    data = readDataFromDatabase(code)
    dateList = [i[8] for i in data]
    openValue = [i[2] for i in data]
    closeValue = [i[3] for i in data]
    highValue = [i[4] for i in data]
    lowValue = [i[5] for i in data]
    d = [openValue, closeValue, highValue, lowValue]
    data = np.transpose(np.array(d))
    cciList = calculateCCI(data, 14)
    anliaze(closeValue, cciList, code)
