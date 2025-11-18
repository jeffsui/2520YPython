"""
字符串函数
"""

# 大小写转换
str1 = "wWW.asJy.coM"
print(str1.upper())
print(str1.lower())
print(str1.title())
print(str1.capitalize())
print(str1.swapcase())

############
# 字符串格式化
############
words = "asjy"
print(words.center(10, "*"))
print(words.ljust(10, "$"))
print(words.rjust(10, "@"))
print(words.zfill(6))

################
# split(separator)
# 将一个字符通过分隔符,转成列表
################
str4 = "科幻,恐怖,剧情"
list_str = str4.split(",")
print(list_str)

##############
# join(list)
# 将一个列表元素拼接成一个字符串
#
##############
list1 = ["美国", "日本", "中国"]
print("-".join(list1))

##################
# 查找元素:
# index(ele): 若未找到,报错
# find(ele): 若未找到,返回-1
# count(ele): 重复的次数
#################
str5 = "www.asjy.com;www.asjy.net"
print(str5.find("asjy"))
print(str5.find("org"))
print(str5.count("asjy"))

#############
# 替换 replace(old,new)
################

paragraph = "If you do much work on computers, eventually you find that there’s some task you’d like to automate. For example, you may wish to perform a search-and-replace over a large number of text files, or rename and rearrange a bunch of photo files in a complicated way. Perhaps you’d like to write a small custom database, or a specialized GUI application, or a simple game"
words_list = paragraph.split(" ")
print(words_list)
an_paragraph = []
for word in words_list:
    an_paragraph.append(word.replace(",", "").replace("?", ""))
print(len(an_paragraph))
# Ex5
words = "a can can can a can"
dict_words = {}
for i in words:
    dict_words[i] = words.count(i)
print(dict_words)
list_value = list(dict_words.values())
max_value = max(list_value)
print(max_value)
for k, v in dict_words.items():
    if v == max_value:
        print("出现频率最高字母:", k, "出现次数", v)

###########
# 字符串格式化
# 1. c-style
# %s 字符串
# %d 整数
# %f 小数   %.2f 小数保留两位小数
# 2. format()
# 格式化函数
# 3. f-string
###########
name = "Jack"
age = 19
score = 98.765
print("名字:%s,年龄:%d,成绩:%.2f" % (name, age, score))
print("名字:{},年龄:{},成绩:{:.2f}".format(name, age, score))
print(f"名字:{name},年龄:{age},成绩{score:.2f}")

##########
# 判断单个字符是字母、数字、空格
#########
poam = "fdsa 1d:j23.b8c9 pecl"
alpha_list = []
digit_list = []
space_count = 0
for i in poam:
    if i.isalpha():
        alpha_list.append(i)
    elif i.isdigit():
        digit_list.append(i)
    elif i.isspace():
        space_count += 1
    else:
        print("other char", i)
print(f"字母{len(alpha_list)},数字{len(digit_list)},空格{space_count}")
