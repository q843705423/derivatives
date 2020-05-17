# -*- coding:utf-8 -*-
import os

import numpy as np
import CCIOb
import time

import struct


def get_file_size(f):
    f.seek(0, 2)
    return f.tell()


def byte_to_int(b):
    return struct.unpack('<I', b)


def get_stock_price_and_date(f):
    size = get_file_size(f)
    stock_length = int(size / 32)
    # begin_time = time.time()
    array = []
    if stock_length < 100:
        return 1, 1
    for i in range(size - 100 * 32, size, 32):
        for j in range(0, 32, 4):
            file.seek(i + j, 0)
            read = file.read(4)
            to_int = byte_to_int(read)
            array.append(to_int)
    stock_arr = np.array(array).reshape(-1, 8)
    # end_time = time.time()
    # print("spend time", end_time - begin_time)
    return stock_arr[:, 1:5], stock_arr[:, 0]


def is_ok(fp="D:/my_app/txdjrzd/app/vipdoc/sz/lday/sz000001.day"):
    index = fp.index(".")
    rindex = fp.rindex('/')
    code = fp[rindex + 1:index]
    # print(file_path)
    # match = re.match("day(.*)", file_path)
    # match = re.match("/(.*?)day", file_path)
    # if match:
    #     print(match.group(1))
    # code = match.group(1)
    # print(code)
    # else:
    # print("not match")
    global file, t
    file = open(fp, "rb")
    price, date = get_stock_price_and_date(file)
    if price == date == 1:
        return
    cciList = CCIOb.calculateCCI(price, 14)
    cciListLen = len(cciList)
    times = [0 for x in cciList]
    t = 0
    for i in range(1, cciListLen):
        if cciList[i - 1] < -100 < cciList[i]:
            t += 1
            times[i] = t
            # print("%s rush -100, and t:" % date[i], t)
        elif -0 < cciList[i]:
            if t != 0:
                t = 0
                times[i] = t
                # print("%s reset value" % date[i])
    if times[cciListLen - 1] >= 2 and 0 >= cciList[cciListLen - 1]:
        print(code, times[cciListLen - 1])


if __name__ == '__main__':
    # file_root = "D:/my_app/txdjrzd/app/vipdoc/sz/lday/"
    file_root = "D:/my_app/txdjrzd/app/vipdoc/sh/lday/"
    file_path_list = os.listdir(file_root)
    num = 0
    begin_time = time.time()
    for file_path in file_path_list:
        num += 1
        real_path = os.path.join(file_root, file_path)
        is_ok(real_path)
        if num % 1000 == 0:
            end_time = time.time()
            print("ok %s stock, spend time:%s" % (num, end_time - begin_time))

        # break

    # is_ok()
