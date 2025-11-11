"""
求 1- 100 的和
"""

"""
n = 1
res = 0
while n <= 100:
    res += n
    # print(n, end=" ")
    n += 1
    # print(res)
print(res)
"""
"""
求 1- 100 的奇数和 偶数和
"""
n = 1
res_odd = 0
res_even = 0
while n <= 100:
    if n % 2 != 0:
        res_odd += n
    else:
        res_even += n
    n += 1
print("odd result ", res_odd)
print("even result ", res_even)
