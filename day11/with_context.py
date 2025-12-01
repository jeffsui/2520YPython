"""
执行上下文 :
在一些需要打开资源的操作中,with修饰的操作
自动调用该对象的close方法执行资源关闭
"""

with open("./day10/myshape.py", mode="r", encoding="utf-8") as f:
    all_lines = f.readlines()
    print(all_lines)
