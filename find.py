import os
import re

listdir = os.listdir("D:/newstock/")
listResult = []
for name in listdir:
    matchResult = re.match("(.*)_result.txt", name, 0)
    if matchResult:
        group = matchResult.group(0)
        listResult.append(group)

print(listResult)


def hello(fileName):
    d = []
    with open(fileName, "r") as f:
        ls = f.readlines()
        for i in range(0, 20):
            index = ls[i].index("为")
            i__index = ls[i].index("%", index)
            d.append(float(ls[i][index + 1:i__index]))
    leftVal = 0.0
    rightVal = 0.0
    for i in range(0, 10):
        # print(d[i])
        leftVal += d[i]

    for i in range(10, 20):
        rightVal += d[i]
        # print(d[i])
    val_ = rightVal / (leftVal + rightVal)
    return val_


m = []
for i in range(len(listResult)):
    f = "D:/newstock/" + listResult[i]
    m.append({"f": f, "value": hello(f)})
    values = hello(f)
    # print(f, values)
    # if values is not None and values > 0.7:
    #     print(f, values)

newlist = sorted(m, key=lambda x: x['value'])
stop = len(newlist)
for i in range(0, stop):
    print(newlist[i]['f'],newlist[i]['value'])
# for i in range
