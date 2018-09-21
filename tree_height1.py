# coding=utf-8
import sys
import re
import random


# 递归返回叶子的位置，即高度
def get(x):
    try:
        return 1 + get(dic_s[x])
    except KeyError:   # 找到根的时候是查不到以根为孩子的记录的
        return 1


n = int(sys.stdin.readline().strip())    # 去除特殊字符
dic_s = {}
for i in range(int(n)-1):
    father, child = sys.stdin.readline().strip().split()   # 父 子
    dic_s[child] = father
temp1 = set(dic_s.keys())
temp2 = set(dic_s.values())
temp = set(dic_s.keys()) - set(dic_s.values())
temp3 = [get(i) for i in set(dic_s.keys()) - set(dic_s.values())]
print max([get(i) for i in set(dic_s.keys()) - set(dic_s.values())]) if n>1 else 1
