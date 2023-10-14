list_num = [1, 3, 4, 3, 7, 3, 9, 8, 6, 3]
for i in range(list_num.count(3)):
    print(list_num.index(3))
    list_num.remove(3)
print(list_num)