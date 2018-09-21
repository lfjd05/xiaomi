# coding=utf-8
def mut_input():
    n = [int(each) for each in raw_input().split()]
    a = []
    while n[0] > 0:
        a.append([each for each in raw_input().split()])
        n[0] -= 1
    return a
a = mut_input()

num = [0]*10
# 遍历每个n
for number in a:
    number = list(str(number[0]))
    # 0 eight
    num[0] = number.count('G')
    # 8 six
    num[8] = number.count('X')
    # 2 zero
    num[2] = number.count('Z')
    # 4 two
    num[4] = number.count('W')
    # 5 three
    num[5] = number.count('H')-num[0]
    # 6 four
    num[6] = number.count('U')
    # 7 five
    num[7] = number.count('F')-num[6]
    # 9 seven
    num[9] = number.count('S')-num[8]
    # 3 one
    num[3] = number.count('O')-num[2]-num[4]-num[6]
    # 1 nine
    num[1] = number.count('I')-num[7]-num[8]-num[0]
    s = ''
    for i in range(10):
        s += str(i)*num[i]
    print s
