"""
day9.advance_function 的 Docstring

map(func,iterable): 将函数,作用在可迭代对象每个元素上


filter(func,iterable): 将函数,作用在可迭代对象每个元素上
函数的返回值bool类型,满足函数的元素保留

reduce(func,iterable): 将函数作用在可迭代对象每个元素,返回的一个结果(递归)

"""

from functools import reduce

L = list(range(1, 11))
# print(L)
print(list(map(lambda x: x**2, L)))
# print([i**2 for i in range(1, 11)])

L = [56, 98, 100, 78, 88, 42, 60, 66]
print(list(filter(lambda x: x >= 60, L)))

L = list(range(1, 11))
print(reduce(lambda x, y: x + y, L))
print(reduce(lambda x, y: x * y, L))
