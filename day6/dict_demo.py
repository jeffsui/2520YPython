"""
           创建 可变类型 key不重复 没有索引 排序
字典(k:v)   {}    是      是

"""

#######
# 如何创建字典
##########
D = {"name": "诸葛亮", "age": 290}
print(D, type(D), len(D))
###############
# 访问字典元素
# D[key] :若key不存在,则报错: KeyError: 'age1'
# D.get(key):若key不存在,返回None,不报错
################
print(D["name"], D["age"])
print(D.get("name"), D.get("age1"))

#################
# 新增|修改
# D[key] = value :若key存在,则修改
# D[key] = value :若key不存在,则新增
################
D["name"] = "司马懿"
print("修改后字典", D, len(D))
D["address"] = "魏国"
print("修改后的字典", D, len(D))
#############
# 判断 key 存在
# key in D  :若存在,则返回True;反之亦然
# key not in D :如果不存在,则返回True;反之亦然
#############
print("city" in D)
print("address" not in D)
###############
# 删除
# pop(key): 根据制定的key删除
# popitem() : 删除最后一个元素
# del D[key] :根据指定的key删除
###############
D.pop("age")
print(D, len(D))
D.popitem()
print(D, len(D))
del D["name"]
print(D, len(D))
############
# 清空 clear
###########
D.clear()
print(D, len(D))

###############3
# 字典遍历（3种）
#############
D = {2: "a", 1: "c", 3: "b"}
print("===遍历字典所有key====")
for k in D.keys():
    print(k, end=" ")
print()
print("===遍历字典所有value====")
for v in D.values():
    print(v, end=" ")
print()
print("===遍历字典所有key:value====")
# [(3, 'a'),(1, 'c'),(2, 'b')]
for k, v in D.items():
    print(k, v, end=" ")
print()

###############
#  字典排序( key * ,value )
#############
print("=====字典排序=========")
list_keys = list(D.keys())
print(list_keys)
list_keys.sort(reverse=True)  # 给key进行原地排序
print(list_keys)
# 遍历排序后 key构成的列表
sorted_dict = {}
for k in list_keys:
    # print(k, D[k])
    sorted_dict[k] = D[k]
print("sorted dict", sorted_dict)

##########
# 字典排序 lambda表达式
#############
print("======字典排序正确方式===========")
print(
    dict(sorted(D.items(), key=lambda item: item[1], reverse=False)),
)
print(
    dict(sorted(D.items(), key=lambda item: item[0], reverse=False)),
)
