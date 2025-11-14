""" """

list1 = [4, 2, 1, 3, 5, 7]
n = len(list1)
print("before sort", list1)
for i in range(n - 1):
    for j in range(n - i - 1):
        if list1[j] > list1[j + 1]:
            # temp = list1[j]
            # list1[j] = list1[j+1]
            # list1[j+1] = temp
            list1[j], list1[j + 1] = list1[j + 1], list1[j]
print("after sort", list1)
