"""
元组解构
复杂类型,逗号分隔,将元组解构数据 拆包
*rest 剩余元素
_ 一个元素
"""

tuple_info = (10, 20, 30)
# print(tuple_info[0], tuple_info[1], tuple_info[2])
a, b, c = tuple_info
print(a, b, c)

a, *rest, c = tuple_info
print(a, rest)
b = rest
print(b, c)

a, _, b = tuple_info
print(a, b)
print(_)

nested_tuple = ((1, 2), (3, 4))
(a, b), (c, d) = nested_tuple
print(a, b, c, d)
