"""
函数参数:
1. 位置参数
定义函数时候,设定参数(个数、类型、顺序)
调用的时候,根据你参数定义,传递参数,不能多,不能少
2. 默认参数 default
定义函数的时候,给某个参数设定了默认值
rules:  non-default argument follows default argument
没有默认值的参数不能跟在有默认值参数的后面
3. 关键字参数 key-word argument
调用函数的时候用  param=value 这样的方式进行传参
rules: SyntaxError: positional argument follows keyword argument
位置参数不能在关键字参数的后面

4. 可变参数
参数定义  参数前面 *,代表0个 1个 或者任意个参数
这里的参数 被当作元组解析
例如: print()

5. 可变关键字参数
参数定义  参数前面有**,代表0个 1个 或者任意个参数
调用的时候方式 key1=value,key2=value2,.....
**kwargs : 被当作字典解析
rule: arguments cannot follow var-keyword argument
可变参数 不能跟在关键字可变参数的后面
"""

# 位置参数
"""
def add(a: int, b: int):
    print(a + b)

add(1, 2)


# 默认参数
def add(a: int = 10, b: int = 10):
    print(a + b)


add()
add(10)
add(1, 2)



# 关键字参数
def add(a: int, b: int):
    print(f"{a}+{b}={a + b}")


add(1, 2)
add(a=10, b=20)
add(b=3, a=5)
# add(a=1, 20) # 报错 SyntaxError: positional argument follows keyword argument
# add(w=3, x=9)

# print(1, "GTrue", 12.35, True)


# 可变参数实例
def add(*args):
    print(args, type(args))
    for i in args:
        print(i)


# add()
# add(1, 2)
# add(1, 2, 3)



# 关键字可变参数
def info(**kwargs):
    print(kwargs, type(kwargs))
    for k, v in kwargs.items():
        print(f"参数{k}的值是{v}")


info(name="Jack", age=19, score=98.56)
"""


def show(
    a,
    b=3,
    c=5,
    *args,
    **kwargs,
):
    print(f"a={a}, b={b}, c={c} args={args}, kwargs={kwargs}")


# show(1, 2, 3, c=9)
# show(1, 2, 3, 4, 5, d=9)
show(1)
show(1, 2, 3)
show(1, c=9)
show(1, b=99, c=100)
show(1, 3, 4, 5, 6, 7, d="aaa")
