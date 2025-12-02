"""
day12.random_demo
1. random.random()
0 - 1 之间随机小数
2. randint(n, m)
n - m 之间的随机整数
3. randrange(n, m,s)
n - m 之间,每s个的随机整数
4. choice(iterable)
从可迭代对象中随机选择一个元素
5. shuffle(iterable)
将可迭代对象元素乱序
6. uniform(n,m)
n-m之间的随机小数
"""

import random

for i in range(4):
    randnum = random.random()
    print(randnum, end=" ")
print()
for i in range(4):
    print(random.randint(1, 10), end=" ")
print()

for i in range(4):
    print(random.randrange(0, 10, 2), end=" ")
print()


for i in range(4):
    print(random.uniform(2, 4), end=" ")
print()

L = [88, 77, 66, 99]
print(random.choice(L))
story = ["古代", "英雄", "王子", "公主", "森林", "恶龙", "传说", "魔法"]

random.shuffle(story)
print(" ".join(story))

# round 四舍五入

number_float = 3.1415926
print(round(number_float, 3))
