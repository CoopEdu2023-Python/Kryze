def check(a):
    if len(a) > 1 and a.find('-', 0, len(a) - 1):
        return False
    if len(a) > 1 and a[0] == '0':
        return False
    for i in a:
        if i < '0' or i > '9':
            return False
    return True
m = input("输入M")
n = input("输入N")
while (not check(m)) or (not check(n)):
    print("非法输入")
    m = input("输入M")
    n = input("输入N")
n = int(n)
s = 0
for i in range(n):
    add = m * (i + 1)
    # print(add)
    s += int(add)
print(s)