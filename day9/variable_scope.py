"""
day9.variable_scope 的 Docstring
变量的作用域
1. 全局作用域
声明在函数外面的变量
2. 局部作用域
声明在函数里的变量

tips:
1. 局部作用域 无法修改全局作用域的变量

global: 将局部提升为全局

"""

num = 10


def show():
    global num
    num = num + 1
    print("funcion :", num)


print(f"before fun calling num={num}")
show()
print(f"after fun calling num={num}")
