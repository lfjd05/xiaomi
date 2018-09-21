# coding=utf-8
"""
思路：用字典做数据结构，统计每个节点的所在层数和子节点数，返回最大层数
"""


def mut_input():
    n = [int(each) for each in raw_input().split()]
    a = []
    while n[0]-1 > 0:
        a.append([int(each) for each in raw_input().split()])
        n[0] -= 1
    return a


tree = {0:[1, 0]}   # 节点0， 层数，孩子个数
# data = mut_input()
# data = [[0,1],[0,2],[1,3],[1,4]]
data = [[2,3],[3,0],[3,4],[1,2]]
for node in data:
    father, child = node   # 一条父子记录
    if father in tree and tree[father][1]<2:   # 如果该节点已经在树里面并且孩子不满
        tree[father][1] += 1    # 为他添加一个孩子
        # child location
        height = tree[father][0] + 1
        tree[child] = [height, 0]  # 把这条记录的孩子加到树里面

print max([a[0] for a in tree.values()])
