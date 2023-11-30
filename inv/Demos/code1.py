list_1 = list()


for i in range(1, -1, -1):
    list_1.append(str(i))


list_2 = '0'.join(list_1)
print(list_2)


list_3 = list_2[:-1:]
print(list_3)

list_3.replace('0', '1')
print(list_3)