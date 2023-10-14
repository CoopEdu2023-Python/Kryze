line = input("以空格分开")
list = line.split()
for i in range(len(list)):
    list[i] = int(list[i])
while len(list) > 1:
    list.append(list.pop(0) * list.pop(0) + 1)
    list.sort()
print(list[0])
