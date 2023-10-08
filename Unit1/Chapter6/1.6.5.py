def diamond(h):
    rt = ""
    mid = h // 2
    f = True
    if h == mid * 2:
        f = False
    for i in range(1, mid + 1):
        for j in range(0, abs(i - mid) + 1 - (not f)):
            rt += " "
        for k in range(1 + (i - 1) * 2):
            rt += "*"
        rt += "\n"
    if f == True:
        for k in range(1 + mid * 2):
            tr += "*"
        rt += "\n"
    for i in range(mid + 1 + f, h + 1):
        for j in range(0, abs(i - mid) - 1):
            rt += " "
        for k in range(1 + (h - i) * 2):
            rt += "*"
        rt += "\n"
    return rt
print(diamond(10))
