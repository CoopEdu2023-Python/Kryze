def harmonic_sum(current_sum):
    if current_sum == 0:
        return 1
    else:
        return 1 / (current_sum + 1) + harmonic_sum(current_sum - 1)


n = int(input())
print(harmonic_sum(n - 1))