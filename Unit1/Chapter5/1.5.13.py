sum = [0, 0]
for i in range(1, 101):
    sum[i % 2] += i
print(f"The sum of the even number is {sum[0]}")
print(f"The sum of the odd number is {sum[1]}")