list = []
l = [0, 0, 0, 0, 0, 0]
r = [0, 0, 0, 0, 0, 0]
for i in range(6):
        list.append([])
for i in range(6):
    for j in range(6):
        list[i].append(0)
for i in range(6):
    line = input()
    list[i] = line.split()
    for j in range(6):
        list[i][j] = int(list[i][j])
        l[i] += list[i][j]
        r[j] += list[i][j]
for i in range(6):
    print(f"第{i + 1}行的和为{l[i]}")
for i in range(6):
    print(f"第{i + 1}列的和为{r[i]}")