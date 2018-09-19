# coding=utf-8
# 多行输入输出程序


def mut_input():
    n = [int(each) for each in raw_input().split()]
    a = []
    while n[0] > 0:
        a.append([each for each in raw_input().split()])
        n[0] -= 1
    return a


def mut_out(a):
    for line in a:
        print " ".join(str(i) for i in line)


s = mut_input()
mut_out(s)
