def print_perfect_number() -> None:
    for raw in range(1, 1001):
        num = raw
        sum_div = 0
        for i in range(1, num // 2 + 1):
            if num % i == 0:
                sum_div += i
        if sum_div == raw:
            print(raw)


print_perfect_number()
