num = int(input())
i = 2
print(f"{num} =", end = " ")
while not num == 1:
    if num % i == 0:
        print(i, end = " ")
        num /= i
        if not num == 1:
            print("*", end = " ")
    else:
        i += 1