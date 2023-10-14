n = int(input("元素数量"))
list = []
for i in range(n):
    list.append(input("输入元素"))
i = 1
while i <= n * 2:
    list.insert(i, 0)
    i += 2
print(list)