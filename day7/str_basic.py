"""
str 声明方式
转义字符
\n 强制换行
\t 制表符
str 是一种不可变类型

str 支持切片操作

str 常用的函数
"""

str1 = "asjy"
str2 = "www.asjy.org;www.asjy.com"
str3 = """床前明月光,
疑是地上霜。
举头望明月,
低头思故乡。"""
print(str2)
print(str3)
#############
# 字符串: 字符序列
# 通过索引访问字符串的元素
###############
print(str1[0])
print(str1[len(str1) - 1])
for i in str1:
    print(i, end=" ")
print()
# str1[0] = "A"
###############
# 字符切片
# str[n:]
# str[n:m]
# str[n:m:s]
# 特殊  str[::-1]
###################
print(str2[4:])
print(str2[4:12])
print(str2[::-1])
