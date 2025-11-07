"""
输入年份:
判断是不是闰年
条件:
1. 逢4必闰 并且 逢100不闰
2. 逢400又闰
分析:
(year%4==0 and year %100!=0) or (year%400==0)
"""

year = int(input("input year:"))
print((year % 4 == 0 and year % 100 != 0) or (year % 400 == 0))
