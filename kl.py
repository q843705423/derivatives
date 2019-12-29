# 凯莉公式
def sgm(p, r, f):
    res = 0
    len1 = len(p)
    for j in range(0, len1):
        one = p[j]*r[j]/(r[j]+f*r[j])
        res += one
    return res


p = [0.5, 0.5]
r = [0.3, -0.1]
stop = 1000000
print(p, r, 0.333333333)
print(sgm(p, r, 0.333333333))
# for i in range(0, stop, 1):
#
#     values = sgm(p, r, i * 1.0 / stop)
#     values2 = sgm(p, r, (i - 1) * 1.0 / stop)
#     if values2 > 0 and values < 0:
#         print(i / stop * 100.0, "%")
#         break
#     if values > 0 and values2 < 0:
#         print(i / stop * 100.0, "%")
#         break
#     # print(values)
#     # print(i, values)
