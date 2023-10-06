while True:
    num = int(input())
    print(f"The factors of {num} are :")
    f = 2
    while not num == 1 and f <= num:
        if  num % f == 0:
            print(f, end = " ")
        f += 1
    print("\n__________________________")