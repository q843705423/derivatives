import numpy as np

# 实现将数据从csv文件中导入到python内存中

arr = np.loadtxt("dataX.txt")
print(arr)

# 看是否可以为数组添加一列
arr = np.column_stack((arr, np.ones(arr.shape[0])))
print(arr)



