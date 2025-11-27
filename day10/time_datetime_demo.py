"""
time 模块演示
time.time(): 获取1970年到现在的时间戳（秒数，浮点数包含小数部分）
time.sleep(): 暂停执行指定的秒数

datetime模块

"""

import datetime
import time
from datetime import timedelta

# 获取开始时间戳
begin = time.time()
print(f"开始时间戳: {begin}")

# 暂停2秒
print("暂停2秒...")
# time.sleep(2.0)

# 获取结束时间戳并计算时间差
end = time.time()
elapsed_time = end - begin
print(f"结束时间戳: {end}")
print(f"经过时间: {elapsed_time:.2f}秒")
# 生成格林威治时间
localtime = time.asctime(time.localtime(time.time()))
print(localtime)

# 日期格式化
print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))

# 获取当前时间
today = datetime.datetime.today()
print(today)


# 获取当前时间
now = datetime.datetime.now()
# 时间偏移
print("yesterday", today + timedelta(days=-1))
print("tommorrow", today + timedelta(days=1))
print("1 hour after", now + timedelta(hours=1))
print("30 min before", now + timedelta(hours=-0.5))
