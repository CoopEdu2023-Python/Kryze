ans = 81
res = 0
while not ans == res:
    res = int(input("input the number you guess:"))
    if ans == res:
        print("Correct")
        break
    if abs(ans - res) >= 50:
        print("Not even close")
    elif abs(ans - res) >= 30:
        print("Wrong")
    elif abs(ans - res) <= 10:
        print("Close")
    else:
        print("not greater than 30")