"""
学校运动会
进入男子组决赛 9.8 , 未进入男子组决赛
进入女子组决赛 10.2, 未进入女子组决赛
额外: 输入性别有误,显示 成绩无效


gender = input("sex:")
score = float(input("score:"))
if gender == "m":
    if score <= 9.8:
        print("man final test")
    else:
        print("not man final test")
elif gender == "f":
    if score <= 10.2:
        print("femal final test")
    else:
        print("femal man final test")
else:
    print("wrong sex no score")
"""

gender = input("sex：")
score = float(input("score:"))
if gender == "m":
    if score <= 9.8:
        print("man final test")
    else:
        print("not man final test")
else:
    if gender == "f":
        if score <= 10.2:
            print("femal final test")
        else:
            print("femal man final test")
    else:
        print("wrong sex no score")
