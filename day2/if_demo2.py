"""
输入三个数字,最大的数

分支嵌套使用
if 条件1:
    if 条件2:
       ..
    else:
       ..
else:
实际情况,嵌套分支应用场景更广泛
"""

a = int(input("a:"))
b = int(input("b:"))
c = int(input("c:"))

# max_num = a
# if a > b:
#     max_num = a
# else:
#     max_num = b

# if c > max_num:
#     max_num = c

max_num = 0
if a > b and b > c:
    max_num = a
else:
    if a < b and b < c:
        max_num = c
    else:
        max_num = b
print("max num", max_num)
