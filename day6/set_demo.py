"""
集合
     创建 可变类型 无序 元素唯一(去重) 没有索引
set  {}     是    是    是           是
"""

#########
# set创建
##############
a = {"1", "2", "3"}
print(a, type(a), len(a))

###############
# 新增
# add(ele)
#############
a.add("4")
print(a, len(a))
##############
# update(other_set)
#############
other_set = {"5", "6", "4"}
a.update(other_set)
print(a, len(a))
##########
# 删除
# pop()
# discard()
# remove()
#########
print("随机删除", a.pop())
print(a)
# print(a.discard("1"))
# print(a, len(a))
# a.remove("2")
# print(a, len(a))
