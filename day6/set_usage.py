"""
集合运算
并集
交集
差集
补集(对称差集)

集合关系
"""

s1 = {"1", "3", "4", "5"}
s2 = {"4", "6", "7", "8"}
s3 = {"1", "3", "5"}
# 并集
print("并集", s1 | s2)
print("交集", s1 & s2)
print("差集", s1 - s2)
print("差集", s2 - s1)
print("补集", s1 ^ s2)
######
# 父集
# 子集
##########
print("子集：", s3 < s1, s3.issubset(s1))
print("父集:", s1 > s3, s1.issuperset(s3))
print("1" in s1)
print("3" not in s2)
