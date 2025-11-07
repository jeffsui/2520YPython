"""
比较运算符
> >= < <= == !=

逻辑运算符

and : 并且, 两个条件如果都为True,则结果也为True;两个条件只要有一个为False,结果就为False
or : 或者, 两个条件只要有一个条件是True,结果就是True;两个条件均为False,结果才是False
not : 逻辑取反

tips:
短路与: 如果第一个条件为False,结果一定是False,后面就不用判断了

逻辑表达式 : 结果bool类型  True | False
5>3
"""

a = 10
b = 5
c = 10
print(a > b)
print(a < b)
print(a == b)
print(a == c)
print("=" * 10)
print(a > 5 and b < 10)
print(a > 10 and b < 10)
print(a > 5 and b < 5)
print(a > 10 and b < 5)
print("*" * 10)
print(a > 5 or b < 10)
print(a > 10 or b < 10)
print(a > 5 or b < 5)
print(a > 10 or b < 5)
print("==Not===")
print(not (a > b))
print(not (a < b))
