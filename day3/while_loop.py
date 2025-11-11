"""
break:
根据条件,退出当前循环以及后面的所有循环

无限循环
1. 不知道循环次数的情况下
2. 统计输入数字总和
3. 限定:
   输入0 退出循环
   是否继续(y/n): 不是y 退出



n = 1
res = 0
while True:
    number = int(input("number:"))
    res += number
    n += 1
    if number == 0:
        break  # 提前终止循环

print(n, "个数字的和:", res)
"""

n = 0  # 计数器
res = 0  # 存储所有数字的和
flag = True
# 注意：下面变量的初始值用于在循环中更新最小值和最大值。
# 将 max_number 设为正无穷，这样第一个输入的数字会小于它，从而把它更新为真实的最小值。
# 将 min_number 设为负无穷，这样第一个输入的数字会大于它，从而把它更新为真实的最大值。
# 变量命名上有点容易混淆（max_number 实际上先被用于记录最小值），这里只保留原逻辑并做注释说明。
max_number = float("inf")  # 用作初始最小值的占位（开始为 +inf）
min_number = float("-inf")  # 用作初始最大值的占位（开始为 -inf）
while flag:
    number = int(input("number:"))
    # 更新最小/最大值
    # 如果当前输入小于 max_number（初始为 +inf），则更新为更小的值
    if number < max_number:
        max_number = number
    # 如果当前输入大于 min_number（初始为 -inf），则更新为更大的值
    if number > min_number:
        min_number = number

    # 将输入加入总和并增加计数
    res += number
    n += 1

    # 询问是否继续：只有输入 'y'（严格小写）才继续，否则退出循环
    exit = input("是否继续(y/n)?")  # 是否继续
    if exit != "y":
        # break  # 提前终止循环
        flag = False
print(n, "个数字的和:", res)
print("max number", max_number, "min number", min_number)
