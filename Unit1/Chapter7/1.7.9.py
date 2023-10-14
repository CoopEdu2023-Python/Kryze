def cal(list, level):
    list = list[2:-2]
    s = sum(list)
    return s * level
list = list()
for i in range(7):
    list.append(int(input("裁判打分")))
list.sort()
level = float(input("难度系数"))
print("%.2f" % cal(list, level))

