import struct
import numpy as np

COL_DATE = 0
COL_OPEN = 1
COL_HIGH = 2
COL_LOW = 3
COL_CLOSE = 4
COL_AMOUNT = 5
COL_VOL = 6
COL_RESERV = 7

# 移动平均时间
AVG_DAY = 14
file = open("D:/my_app/txdjrzd/app/vipdoc/sz/lday/sz002310.day", "rb")
dataList = []
while True:
    data = file.read(4)
    if len(data) == 4:
        x = struct.unpack('i', data)
        # print(x)
        dataList.append(x)
    else:
        break

M = np.reshape(dataList, [-1, 8])
[rowM, colM] = M.shape
# 计算TP 即为最低价,最高价,收盘价的均值
TP = (M[:, COL_HIGH] + M[:, COL_LOW] + M[:, COL_CLOSE]) / 3

# 计算MA TP的滑动平均值
# for i in range(AVG_DAY, )
MA = []
for i in range(AVG_DAY - 1):
    MA.append(0)
firstMA = np.array(TP[0: AVG_DAY]).sum(0) / AVG_DAY
MA.append(firstMA)
for i in range(AVG_DAY, rowM):
    print(i)
    ma = TP[i - AVG_DAY: i - 1].sum(0) / AVG_DAY
    MA.append(ma)

# subMA = TP[0: rowM - AVG_DAY]
# addMA = TP[AVG_DAY:]
# additionalMA = firstMA + (addMA - subMA) / AVG_DAY
# MA = np.column_stack(([np.zeros(AVG_DAY - 1)], [[firstMA]], [additionalMA])).sum(0)

# 计算MD
slideTP = []
for i in range(0, AVG_DAY - 1):
    slideTP += [[0] * AVG_DAY]

MD = []
for i in range(AVG_DAY):
    MD.append(0.001)

for i in range(AVG_DAY, rowM):
    MD.append(np.array(np.abs(TP[i - AVG_DAY: i - 1] - MA[i])).sum(0) / AVG_DAY)

    # MD.append(np.array(abs(TP[i:i + AVG_DAY] - MA[i])).sum(0) / AVG_DAY)
    # i_ = [TP[i: i + AVG_DAY] - MA[i]]
    # slideTP += i_
    # if i == 30:
    #     print(i_)
CCI = (TP - MA) / MD / 0.015
print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
print(CCI)
print("????????????????????????????????????????????????????????????????????????????????????????????????????")
# slideTP = np.array(slideTP)

# MD = np.abs(np.transpose(slideTP)).sum(0) / 14
# MD = np.abs(np.transpose(slideTP) - MA).sum(0)

# CCI = (TP - MA) / MD / 0.015
# [CCI_row] = CCI.shape
# for i in range(CCI_row):
#     pass
# print(CCI[i])
