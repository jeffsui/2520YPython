"""
python 写入文件

"""

################
# open(file_path,mode,encoding)
# mode = 'w': 如果文件不存在,则新建;如果文件存在,则覆盖
# mode = 'w+': 可读可写入,写入之后光标都会移动到末尾
# mode = "a" 追加
# mode = "ab" 二进制方式追加写入文件
# seek() 调整文件指针
#  write 写入字符串 不包含换行
#  writelines 写入多行字符串,自己有换行符
#
################

handler = open("./day11/demo1.txt", mode="a", encoding="utf-8")
# handler.write("爱尚教育\n")
# handler.seek(0)
# print(handler.readline())
content = """明月几时有,
把酒问青天
"""
handler.writelines(content)
handler.close()
