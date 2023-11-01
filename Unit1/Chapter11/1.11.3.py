def geometric_sum(current_sum):
    if current_sum == 0:
        return 1
    else:
        return 1 / (2 ** current_sum) + geometric_sum(current_sum - 1)


n = int(input())
print(geometric_sum(n))