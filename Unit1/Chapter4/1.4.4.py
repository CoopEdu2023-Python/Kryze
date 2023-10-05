ans = 81
res = 0
while not ans == res:
    res = int(input("输入你的猜测:"))
    if res > ans:
        print("too high")
    elif res < ans:
        print("too low")
    else:
        break
print("猜对了")