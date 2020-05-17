import logicTestV2
import logisticV2
import os
import re
import sys

# date = "20200103"
date = sys.argv[1]
print("-----------------")
print(date)
print("-----------------")

logicXDir = os.listdir("D:/newstock/" + date + "/logicX/")
logicResultDir = os.listdir("D:/newstock/" + date + "/result/")
listX = []
listResult = []
for name in logicXDir:
    matchX = re.match("(.*).txt", name, 0)
    if matchX:
        group = matchX.group(1)
        listX.append(group)

for resultFileName in logicResultDir:
    matchResult = re.match("(.*).txt", resultFileName, 0)
    if matchResult:
        group = matchResult.group(1)
        listResult.append(group)

needList = []
for x in listX:
    ok = 1
    for result in listResult:
        if x == result:
            ok = 0
    if ok == 1:
        needList.append(x)

for need in needList:
    print(need)
    logisticV2.GeneratingParameters(date, need)
    logicTestV2.forecast(need, date)
