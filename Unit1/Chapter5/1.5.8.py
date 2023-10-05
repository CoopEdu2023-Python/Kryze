i = 1
sum = [0, 0]
while i <= 100:
    sum[i % 2] += i
    i += 1
print(f"The sum of even number is {sum[0]}")
print(f"The sum of odd number is {sum[1]}")