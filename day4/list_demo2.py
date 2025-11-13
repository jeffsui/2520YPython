"""
列表实现一个通讯簿管理
1. 先创建一个空列表
2. 实现功能如下:
2.1 新增一个联系人
2.2 查询: 遍历通讯簿
2.3 修改:
2.4 删除:
2.5 退出系统 break
tips:
1. 联系人 名字 不重复
ele in list :True 列表中存在该元素
ele not in list: True 列表中不存在该元素
2. 如何进行检索?
list1.index(ele)--> index 查找元素对应的索引

"""

contact = []
while True:
    print("welcome to my contact app:")
    print("choose your menu:\n1.Add \n2.Update \n3.Delete \n4.Query \n5.Exit")
    choose = input("please input menu num:")
    if choose == "1":
        print("**Add**")
        name = input("input contact name?")
        if name not in contact:
            contact.append(name)
            print("添加成功")
        else:
            print("联系人已经存在,添加失败")
    elif choose == "2":
        print("**Update**")
        name = input("input update contact name?")
        if name in contact:
            index = contact.index(name)  # search name list index
            new_name = input("input updated new name?")
            contact[index] = new_name
            print("修改成功")
        else:
            print("联系人不存在,修改失败")
    elif choose == "3":
        print("**Delete**")
        del_name = input("input delete contact name?")
        if del_name in contact:
            contact.remove(del_name)
            print("删除成功")
        else:
            print("联系人不存在,删除失败")
    elif choose == "4":
        print("**Query**")
        for i in range(len(contact)):
            print(i, contact[i])
    elif choose == "5":
        print("**Exit**")
        break
    else:
        print("Wrong Menu Num,Try again!")
