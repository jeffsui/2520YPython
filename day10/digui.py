"""
函数递归: 函数调用函数自身
1、 不能无限递归,退出递归条件
2、每个编程语言都有递归层数限制 1000
"""
#####
# 输入一个数字,
# 求数字前n项的和
# 例如: 输入10
#      输出前10项的和
# 分析
# 前10项的和 ,10+前9项的和
# ....
# 前n项的和,n+前n-1项的和
# 前1项的和 就是1
########


def getN(n: int) -> int:
    res = 0
    for i in range(1, n + 1):
        res += i
    return res


def getNDigui(n: int) -> int:
    if n == 1:
        return 1
    else:
        return n + getNDigui(n - 1)


print(getN(10))
print(getNDigui(10))


################
# 斐波那契额数列
# 1 1 2 3 5 8 13 21 34 55 89
# 输入n 输出第n项中fib的值
# 分析:
# n=1 n=2 return 1
# fib(n-1)+fib(n-2)
######################
def fib(n: int) -> int:
    if n == 1 or n == 2:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


print(fib(6))
