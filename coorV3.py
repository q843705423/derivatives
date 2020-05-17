import numpy as np
import logisticV3
import logicTestV3
import pymysql


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


def addTp(data):
    ID = 0
    CODE = 1
    OPEN = 2
    CLOSE = 3
    HIGH = 4
    LOW = 5
    length = len(data)
    width = -1
    newData = []
    if length != 0:
        width = len(data[0])

    for i2 in range(0, length):
        for j in range(0, width):
            # print(data[i][CODE])
            d = data[i2] + ((data[i2][CLOSE] + data[i2][HIGH] + data[i2][LOW]) / 3,)
        newData.append(d)

    return newData


def calculate_ma(data):
    TP = 10
    P = 14
    len_data = len(data)
    result = []
    for i3 in range(0, len_data):
        sum = 0.0
        avg = 0.0
        if i3 < P:
            avg = data[i3][TP]
        else:
            for j in range(0, P):
                sum += data[i3 - j][TP]
            avg = sum / P
        r = data[i3] + (avg,)
        result.append(r)
    return result


def calculate_with_md(data):
    MA = 11
    TP = 10
    len_data = len(data)
    P = 14
    result = []
    for ii in range(len_data):
        resultSum = 0.0
        avg = 0.0
        if ii < P:
            avg = 0.1
        else:
            for j in range(0, P):
                resultSum += abs(data[ii - P][MA] - data[ii - j][TP])
            avg = resultSum / P
        r = data[ii] + (avg,)
        result.append(r)
    return result


def calculate_cci(data):
    MA = 11
    TP = 10
    MD = 12
    len_data = len(data)
    result = []
    for i in range(0, len_data):
        cci = (data[i][TP] - data[i][MA]) / (0.015 * data[i][MD])
        r = data[i] + (cci,)
        result.append(r)
    return result


def getData():
    return np.loadtxt('C:/Users/Administrator/Desktop/111.txt')


def test():
    CCI = 13
    MA = 11
    TP = 10
    MD = 12
    DATE = 8
    data = readDataFromDatabase("sh600007")
    data_with_tp = addTp(data)
    data_with_ma = calculate_ma(data_with_tp)
    data_with_md = calculate_with_md(data_with_ma)
    data_with_cci = calculate_cci(data_with_md)
    len_data_with_cci = len(data_with_cci)
    for i in range(0, len_data_with_cci):
        if i > 1900:
            print(
                "----------------------------------------------------------------------------------------------------")
            print("date:", data_with_cci[i][DATE])
            print("CCI:", data_with_cci[i][CCI])
            print("MA:", data_with_cci[i][MA])
            print("MD:", data_with_cci[i][MD])
            print("TypePrice:", data_with_cci[i][TP])
        # break


OPEN = 0
HIGH = 1
LOW = 2
CLOSE = 3
P = 20
if __name__ == '__main__':
    global P
    data = getData()
    typePrice = (data[:, LOW] + data[:, CLOSE] + data[:, HIGH]) / 3.0
    len_typePrice = len(typePrice)
    # print(len_typePrice)
    # print(typePrice)
    MAArr = []
    for i in range(P):
        MAArr.append(0.0)
    for i in range(P, len_typePrice):
        sum_of_type_price = sum(typePrice[i - P, i])
        print(sum_of_type_price)
