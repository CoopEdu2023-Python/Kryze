num = int(input())
flag = True
for i in range(2, num + 1):
    if num % i == 0:
        flag = False
if flag == True or num == 2:
    print("It is a prime number")
else:
    print("It is not a prime number")