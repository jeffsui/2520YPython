"""
extends
"""

list1 = [1, 2, 3]
list2 = [4, 5, 6]
# list1.append(list2)
# for i in list2:
# list1.append(i)
list1.extend(list2)
print(list1)
"""
二维列表
"""
list3 = [[1, 2], [3, 4], [5, 6]]
print(list3)
# print(list3[0])
# print(list3[1])
# print(list3[2])
# 二维列表访问元素
# print(list3[0][1])
# print(list3[2][1])
# 二维列表遍历
# for i in list3:
#     for j in i:
#         print(j, end="\t")
#     print()
# 二维转一维
# L = []
# for i in list3:
#     for j in i:
#         L.append(j)
# print(L)

##################
# 进阶方法
# index(ele)-> index : 查找某个元素列表中出现索引位置
# count(ele) : 统计元素列表中出现的次数
# reverse() : 将列表反转
# sort() : 将列表排序,默认是升序
###############
L = [4, 1, 2, 3, 1, 5, 7, 1]
print(L.count(1))
L.reverse()
print(L)
L.sort()
print(L)
L.sort(reverse=True)
print(L)
