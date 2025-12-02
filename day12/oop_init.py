class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.__score = None  # 不允许你直接访问属性 private attribute

    def show_info(self):
        print(f"{self.name} age is {self.age} score {self.__score}")

    def set_score(self, score):
        self.__score = score

    def get_score(self):
        return self.__score

    def get_degree(self):
        if self.__score >= 90:
            return "A"
        elif self.__score >= 80:
            return "B"
        elif self.__score >= 60:
            return "C"
        else:
            return "D"



if __name__ == "__main__":
    stu1 = Student("Jack", 19)
    stu1.show_info()
    # modidy attribute
    stu1.name = "Mick"
    stu1.age = 20
    # stu1.__score = 100
    stu1.set_score(99)
    stu1.show_info()
    print(stu1.get_degree())

    # 方法 直接获取 对象中所有属性
    print(stu1.__dict__)

    # stu1.name = "Jack"
    # stu1.age = 19
