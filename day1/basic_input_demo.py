##########
# 输入:  名字 年龄 成绩
# 一行 结果： 名字是 Jack, 年龄是 23 岁, 成绩是 98.5 分
#
# print(name,"",)
############
name = input("your name?")
age = input("your age?")
score = input("your score?")
###########
#   format string
################
# print("name is", name, ",age is ", age, "years old, score is", score)
print(f"name is {name},age is {age} years old,score is{score}")
