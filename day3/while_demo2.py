"""
continue:
终止本次循环(未执行完的部分),继续执行下一次循环,直到循环结束
"""

# 1- 10 跳过5
n = 0
while n < 10:
    n += 1
    if n == 5:
        continue
    print(n)
