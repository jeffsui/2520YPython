"""
生成器(generator): 返回可迭代对象的函数
1. 函数中使用yield
"""


def func(list1: list[int]):
    # L = []
    # for i in list1:
    #     if i % 2 == 0:
    # L.append(i)
    # return L
    for i in list1:
        if i % 2 == 0:
            yield i


# g = func([1, 3, 2, 5, 7, 8])
# print(next(g))
# print(next(g))

L = [1, 3, 2, 5, 7, 8]
g_rep = (i for i in L if i % 2 == 0)
print(g_rep)
print(next(g_rep))
print(next(g_rep))
