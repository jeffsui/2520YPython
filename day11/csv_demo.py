"""
csv模块

Reader: 以列表形式存储文件
DictReader: 以字典形式存储文件,csv第一行作为字典的键
"""

import csv

# with open("./day11/demo.csv", mode="r", encoding="utf-8") as f:
#     reader = csv.reader(f)
#     for row in reader:
#         print(row)

with open("./day11/demo.csv", mode="r", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for item in reader:
        print(item["name"], item["age"], item["score"])
