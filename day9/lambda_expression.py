"""
day9.lambda_expression 的 Docstring

lambda x,y.... : return_value
"""

###########
# 2x+y
###########


def fomular(x, y):
    return 2 * x + y


# print(fomular(1, 2))

print((lambda x, y: 2 * x + y)(2, 3))


#############
# 输入一个数字: 判断是奇数还是偶数
# 如果是奇数 返回True
# 反之返回False
##############

"""
def even_or_odd(number) -> bool:
    if number % 2 == 0:
        return True
    else:
        return False

"""


##############
# 三元表达式
# 条件成立返回  if condition else 条件不成立返回
#################
# def even_or_odd(number) -> bool:
#     return True if number % 2 == 0 else False

print((lambda number: True if number % 2 == 0 else False)(9))


############
# lambda 表达式 应用
# 字典排序
#############
D = {"f": 4, "c": 2, "b": 1, "a": 3}

# print(D.keys())
# only support key sort
print(sorted(D))
# default support with key sort
print(dict(sorted(D.items(), reverse=True)))
# [('a', 3), ('b', 1), ('c', 2), ('f', 4)]
print(dict(sorted(D.items(), key=lambda item: item[1], reverse=True)))

###############
# lambda 返回元组
###########
print((lambda x, y: (y, x))(1, 2))
