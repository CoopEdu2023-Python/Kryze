chance = 5
ans = 81
while chance > 0:
    res = int(input("input the number you guess:"))
    if res == ans:
        print("answer correct")
        break
    elif res > ans:
        print("too high")
        chance -= 1
    else:
        print("too low")
        chance -= 1
    if chance == 0:
        print("you fail")
        break