import logicTest
import logistic
import os
import re

listdir = os.listdir("D:/newstock")
listX = []
listResult = []
for name in listdir:
    matchX = re.match("(.*)_logicX.txt", name, 0)
    if matchX:
        group = matchX.group(1)
        listX.append(group)
    matchResult = re.match("(.*)_result.txt", name, 0)
    if matchResult:
        group = matchResult.group(1)
        listResult.append(group)

needList = []
for x in listX:
    ok = 1
    for result in listResult:
        if x == result:
            ok = 0
    if ok==1:
        needList.append(x)

for need in needList:
    print(need)
    logistic.GeneratingParameters(need)
    logicTest.forecast(need)
