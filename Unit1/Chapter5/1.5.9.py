num = int(input())
i = 2
flag = True
while (not num % i == 0) and (i <= num) or (i == 2):
    if num % i == 0:
        flag = 0
        break
    else:
        i += 1
if flag or num == 2:
    print("it is a prime number")
else:
    print("it is not a prime number")