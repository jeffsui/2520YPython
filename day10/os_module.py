"""
os模块
"""

import os
from datetime import datetime

from dateutil.relativedelta import relativedelta

print(os.path.isdir(r"d:\code"))
print(os.path.isfile(r"d:\code\demo.py"))
print(os.path.dirname(r"d:\code\demo.py"))  # 所在文件夹的绝对路径
# 获取文件夹下的文件列表
print(os.listdir("d:/code"))
d = datetime(2025, 1, 31)
one_month_later = d + relativedelta(months=1)
print(one_month_later)
