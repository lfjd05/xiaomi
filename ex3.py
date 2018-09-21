# coding=utf-8
# 德国


def mut_input():
    n, m = [int(each) for each in raw_input().split()]
    a = [int(each) for each in raw_input().split()]
    return a, m, n


# data, m, n = mut_input()
# data, m = [1, 4, 2, 3, 5], 3
data, m, n =[7, 10, 9, 6, 5, 3, 4], 3, 7
gezi = n//m+1
# 最小的一个
# print gezi
b = [data[i:i+gezi] for i in range(0, len(data), gezi)]
# print b
quan = []
for i in b:
    quan.append(sum(i))
print min(quan)
