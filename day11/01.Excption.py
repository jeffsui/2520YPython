"""
Exception:异常

异常处理
1. try... except ...
2. try... except ... finally...
3. try... except ... else... finally...
"""

try:
    print(1 / 0)
except ZeroDivisionError:
    print("除数不能为零异常")
except Exception as e:
    print(f"发生其他异常: {e}")
print(123)
# 索引越界异常示例
# try:
#     L = [1, 2, 3]
#     print(L[3])
# except IndexError:
#     print("列表索引超出范围")

f = None
try:
    print("1.异常语句前....")
    f = open("./day11/demo111.txt", mode="r", encoding="utf-8")
    print("2.异常语句后....")
    f.read()
except FileNotFoundError as e:
    print(f"3. 出现异常:file not found {e}")
else:
    print("4.如果没有异常执行的语句")
finally:
    print("5.无论是否有异常执行:关闭文件")
    if f:
        f.close()
