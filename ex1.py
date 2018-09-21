# coding=utf-8
# 多行输入输出程序


def mut_input():
    n = [int(each) for each in raw_input().split()]
    a = []
    while n[0] > 0:
        a.append([each for each in raw_input().split()])
        n[0] -= 1
    m = [int(each) for each in raw_input().split()]
    return a, m

# data, m = mut_input()
data = [99, 199, 1999, 10000, 39, 1499]
m = 10238

data = sorted(data)

if m > sum(data):
    print 0

# 能否两位组成
if m>data[-1]+data[-2]: # 最大两位数都不行
    if m>data[-1]+data[-2]+data[-3]:  # 最大三位数都不行
        if m>data[-1]+data[-2]+data[-3]+data[-4]:
            if m>data[-1]+data[-2]+data[-3]+data[-4]:
                print 0
            else:
                for p1 in data:
                    for p2 in data:
                        for p3 in data:
                            for p4 in data:
                                for p5 in data:
                                    if p1 + p2 + p3 + p4 + p5 == m:
                                        print 1
        else:
            for p1 in data:
                for p2 in data:
                    for p3 in data:
                        for p4 in data:
                            if p1 + p2 + p3+p4 == m:
                                print 1
    else:
        for p1 in data:
            for p2 in data:
                for p3 in data:
                    if p1 + p2+p3 == m:
                        print 1
else:
    for p1 in data:
        for p2 in data:
            if p1+p2==m:
                print 1
    print 0


