"""
基本类型 str int float bool
name = "Jack"

list1 = ['Jack','mick']
复杂类型(容器类型)  : 一个变量代表多个值
               可变类型 索引  元素可以重复  排序
list 列表 []     是     有
tuple 元组 ()
dict  字典 {}
set   集合 {}
"""

###########
# 列表创建
###########
list1 = ["Kerry", "Mick"]
print(list1, type(list1))
# 长度 len()
print("列表长度:", len(list1))
##############
# 访问第一个元素
# list1[0]
# 索引 范围: 0 - (len-1)
# 索引值 不存在 则报错
###########
print("first element", list1[0])
print("second element", list1[1])
# print("not exist element", list1[99])

###########
# 增加元素
#  append(ele): 追加
###########
list1.append("Kiro")
print("changed list", list1, len(list1))
print("third element", list1[2])
print("last element", list1[len(list1) - 1])

################
# 修改2个元素  Amy
################
list1[1] = "Amy"
print("second element changed to ", list1[1])

###########
# 增加元素
#  insert(index,ele): 在指定index位置,插入元素
###########
list1.insert(0, "Berry")
print(list1, len(list1))
list1.insert(100, "fire")
print(list1, len(list1))

##############
# 删除
# pop() 尾部删除一个元素 append的逆运算
# pop(index) 删除指定的index上的元素
# remove(ele) 删除指定的元素
#################
list1.pop()
print("pop last element", list1, len(list1))
list1.pop(0)
print("pop index position element", list1, len(list1))
list1.remove("Amy")
print("remove(element)", list1, len(list1))

###########
# del list1[0] 删除元素
# del list1 删除列表对象
##############
del list1[0]  # 删除第一个元素 类似 pop(0)
print(list1, len(list1))
# del list1 列表变量 从内存里删除


###############
# clear() 清空列表
#################
list1.clear()
print("清空列表", list1, len(list1))
print(list1)

##############
# 列表遍历
###############
print("=====列表遍历开始============")
T = [4, 1, 3, 2, 7, 5]
for i in T:  # i 代表是 列表中每个元素
    print(i)
print("=====列表遍历结束============")
for i in range(len(T)):  # i-> 列表的索引
    print(i, T[i])
