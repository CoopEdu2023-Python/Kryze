def polynomial(current_sum):
    if current_sum <= 0:
        return current_sum
    return current_sum + polynomial(current_sum - 2)


start = int(input())
print(polynomial(start))