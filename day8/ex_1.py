# 有参数,没有返回值的函数
def f1(a, b, c):
    print(max(a, b, c))


f1(2, 3, 1)


# 有返回值函数
# 【程序2】定义函数f2(a, b)，函数中将两个数之间所有整数和计算后并返回，调用f2函数
# 并输出结果\
"""
def f2(a, b) -> int:
    res = 0
    for i in range(a, b + 1):
        res += i
    return res
"""


def f2(a, b) -> int:
    # L = []
    # for i in range(a, b + 1):
    #     L.append(i)
    # return sum(L)
    # return sum([i for i in range(a, b + 1)])
    L = []
    while a <= b:
        L.append(a)
        a += 1
    return sum(L)


print(f2(1, 10))
