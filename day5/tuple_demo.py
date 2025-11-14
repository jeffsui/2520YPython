"""
       不可变类型  索引  元素重复 排序
元组 ()    是      有     是    可以
"""
############
# 元组创建
############

T = (1, 3, 2, 5, 1)
print(T, type(T))
print("first ele:", T[0])
# T[len(T) - 1], T[-1] 最后一个元素两种写法
print("last ele:", T[len(T) - 1], T[-1])
# T[0] = 9
print(T.count(1))
print(T.index(3))

###########
# 排序
###########
print(sorted(T))


# 字符串格式化
name = "Jack"
age = 19
print("name is {}, age is {} years old".format(name, age))
