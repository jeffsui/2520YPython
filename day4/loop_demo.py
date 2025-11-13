"""
循环嵌套: 循环中还有循环
1. 外层循环执行一次,里层循环执行若干次
2. 外层循环结束,整个循环才结束
"""

# 用循环的方式,输出5行 每行5个*
for i in range(5):  # 外层循环
    for j in range(i + 1):  # 里层循环
        print("*", end="  ")
    print()

# 九九乘法表
for i in range(1, 10):
    for j in range(1, i + 1):
        print(f"{i}*{j}={i * j}", end="\t")
    print()

# 1-4 数字 组成 不重复 3位数 有多少个这样的数字
# 123 321 132 124 133  222 232
res = 0
for i in range(1, 5):
    for j in range(1, 5):
        for k in range(1, 5):
            if i != j and i != k and j != k:
                print(f"{i}{j}{k}")
                res += 1
print(f"总共有{res}个数字")
