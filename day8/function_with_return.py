"""
函数的返回值：
1. 有返回值的函数
return xxx
2. 没有返回值的函数
return None 或没有 return 关键字 return 后面什么都没有
"""

"""

# 有返回值的函数
def add(a, b) -> int:
    return a + b


# res = add(1, 2)
# print(res)
print(add(1, 2))
"""
# L = [4, 6, 1, 2, 5]
# print(sorted(L))
# print(L)
# L.sort()
# print(L)
# 无返回值函数


def show(name) -> None:
    print(f"hello {name}")
    return None


print(show("Jack"))
