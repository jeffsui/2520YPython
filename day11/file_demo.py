"""
python中文件处理
open(file_path,mode,encoding)
参数1: 文件路径
参数2: 打开方式
参数3: 字符编码集
"""

#############
# python\n
# c++\n
# java
# 读取文件
# read() 一次性读取所有文件内容(字符串)
# readline() 一次读一行
# readlines() 一次性读取所有行,存储在list中
##############
handeler = open("./day11/test.txt", mode="r", encoding="utf-8")
print(handeler)
# print(handeler.read())
# print(handeler.readline().replace("\n", ""))
# print(handeler.readline().replace("\n", ""))
# print(handeler.readline().replace("\n", ""))
all_lines = handeler.readlines()
print(all_lines)
handeler.close()
