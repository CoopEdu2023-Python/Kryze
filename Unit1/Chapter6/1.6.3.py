def diamond(h):
    mid = h // 2
    f = True
    if h == mid * 2:
        f = False
    for i in range(1, mid + 1):
        for j in range(0, abs(i - mid) + 1 - (not f)):
            print(" ", end="")
        for k in range(1 + (i - 1) * 2):
            print("*", end="")
        print("\n")
    if f == True:
        for k in range(1 + mid * 2):
            print("*", end="")
        print("\n")
    for i in range(mid + 1 + f, h + 1):
        for j in range(0, abs(i - mid) - 1):
            print(" ", end="")
        for k in range(1 + (h - i) * 2):
            print("*", end="")
        print("\n")
diamond(10)
