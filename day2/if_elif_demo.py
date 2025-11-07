"""
多重分支:


输入成绩: 0 - 100
成绩区间要求:
1. 80 - 100  excellent
2. 70- 80    good
3. 60- 70    passed
4. 0 - 60    failed
除此以外  error


score = int(input("input your score:"))
if score >= 80 and score <= 100:
    print("excellent")
elif score >= 70 and score < 80:
    print("good")
elif score >= 60 and score < 70:
    print("passed")
elif score >= 0 and score < 60:
    print("failed")
else:
    print("error")
"""

score = int(input("score:"))
if score >= 0 and score <= 100:
    if score >= 80:
        print("excellent")
    elif score >= 70:
        print("good")
    elif score >= 60:
        print("passed")
    else:
        print("failed")
else:
    print("error")
