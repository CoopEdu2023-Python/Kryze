num = int(input())
print(f"{num} =", end = "")
for i in range(2, num + 1):
    while num % i == 0:
        num //= i
        print(f" {i}", end = " ")
        if not num == 1:
            print("*", end = "")
    if num == 1:
        break