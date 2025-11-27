############
# calendar 模块
############
import calendar

# 创建一个 TextCalendar 实例，设置每周的第一天为星期日
cal = calendar.TextCalendar(firstweekday=6)
# 生成并打印2024年6月的日历
cal_str = cal.formatmonth(2024, 6)
print(cal_str)
# 检查2024年是否为闰年
is_leap = calendar.isleap(2024)
print(f"2024年是闰年吗? {is_leap}")

# 获取从2000年到2024年之间的所有闰年列表
leap_years = calendar.leapdays(2000, 2025)
print(f"2000年至2024年之间的闰年数量: {leap_years}")

# 获取2024年6月的星期几列表
month_days = calendar.monthcalendar(2024, 6)
print(f"2024年6月的星期几列表: {month_days}")
