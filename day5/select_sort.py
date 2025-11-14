""" """

aList = [4, 1, 3, 2, 7, 5]
n = len(aList)
for i in range(n):  # n索引值
    min_index = i  # i 已排序最小值所在的索引
    for j in range(i + 1, n):
        if aList[j] < aList[min_index]:
            min_index = j
    # 交换两个索引位置上的元素的值
    aList[i], aList[min_index] = aList[min_index], aList[i]
    print(aList)
