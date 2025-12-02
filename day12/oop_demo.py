"""
类: 修士 模板
  属性
  方法(行为):
"""

"""
# baisc class template
class XiuShi:
    def __init__(self):
        self.name = "王林"
        self.level = "练气期"
        self.neili = 10

    def introduce(self):
        print(f"我乃{self.name} 境界{self.level}修士, 气力值{self.neili}")
"""


class XiuShi:
    INSTANCE = "学生类"

    def __init__(self, name, level, neili):
        self.name = name
        self.level = level
        self.__neili = neili  # __开头的属性,无法直接访问(私有属性)

    def introduce(self):
        print(f"我乃{self.name} 境界{self.level}修士, 气力值隐藏")

    def getQili(self):
        return self.__neili


if __name__ == "__main__":
    print(XiuShi, type(XiuShi))
    # 类的实例化 --> create object
    wangSanxiu = XiuShi("天云宗少宗主林若天", "结丹期", 100000)
    print(wangSanxiu, type(wangSanxiu))
    wangSanxiu.introduce()
    print(wangSanxiu.getQili())
    print(wangSanxiu.INSTANCE)
    # print(wangSanxiu.__neili) # 无法访问
    # object  每一个对象都是独一无二的
    ruoxueSanxiu = XiuShi("天云宗护法长老王若雪", "化神期", 1000000000)
    print(ruoxueSanxiu, type(ruoxueSanxiu))
    ruoxueSanxiu.introduce()
