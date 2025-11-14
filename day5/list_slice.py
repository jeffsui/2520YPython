"""
list(): 转成list
list 切片 左闭右开

list[n:] : 从n索引开始到列表结束,生成一个新的列表
list[:m] : 从0开始到m-1索引值结束,生成一个新的列表
list[n:m]: 从n开始m-1结束,生成一个新的列表
list[n:m:s]: 从n开始m-1结束,每2个,生成一个新的列表
list[::-1] 列表反转
list[:] 列表拷贝, 列表复制一份,生成一个新的列表
"""

L = list(range(1, 11))
print(L)
print(L[1:])
print(L[:8])
print(L[2:7])
print(L[::2])
print(L[1::2])
print(L[::-1])
