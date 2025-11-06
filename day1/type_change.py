"""
basic type:
str
int
float
bool

operator :
+  -  * /  //   %  **
和 差 积 商 取整
tips:
-1.  除法 : 两个都是整数,结果都是小数;不能整除的情况下,保留小数近似值

-2. 无论两个数字 只要有一个是小数,结果都是小数

自动类型转换
1. 运算 会自动转换成 小数 形式

强制类型转换
int()
float()
str()
bool()

"""

a = 10
b = 3
print(a + b)  # 两个整数之间 + 连接 : 算术运算符 求和
print(a - b)
print(a * b)
print(a / b)
print(a // b)  # 先做除法运算 取整数部分
print(a % b)  # 除法,取余数部分
print(a**3)  # 幂运算


###########
# 类型转换的错误
# 以10为底 转换 字符串 --> 整数形式
##############
# a = int(input("输入num:"))
# print(a, type(a))
char = "Z"  # ascii  a-z  97 122
# A - Z   65 - 90
print(ord(char))

##############
# 进制转换
#############
num = 10
print(bin(num))  # 0b1010  0b开头
print(oct(num))  # 0o12
print(hex(num))  # 0xa
