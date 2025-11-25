"""
python中的函数不能重复定义(重载)
什么时候 function 需要return
1. return 提前结束函数调用
2. 如果有return xx,将会给其他函数进行调用(作为另一个函数的参数使用)
3. return可以返回任意内容

"""


###########
# 两个数的和的函数：
# 求任意个数求和
# re use
##########
def add(a, b):
    return a + b
    # return None


# def add(a, b, c):
#     print(a + b + c)


# res = add(1, 2)
# print("add 函数返回的内容", res)
# print(add(1, add(2, 3)))


def switch(a, b) -> tuple[int]:
    a, b = b, a
    return [a, b]


print(switch(3, 2))

###############
#
# return 后面没有: 提前终止函数调用
# return 有东西
################


def early_exit(x):
    if x < 0:
        return  # 提前退出，返回 None
    return x * 2


# print(early_exit(-1))
print(early_exit(3))
