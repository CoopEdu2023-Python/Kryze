def print_narcissistic_number() -> None:
    for i in range(1, 10):
        for j in range(10):
            for k in range(10):
                res = pow(i, 3) + pow(j, 3) + pow(k, 3)
                raw = i * 100 + j * 10 + k
                if  res == raw and res % 1000 == res:
                    print(f"{i}{j}{k}")


print_narcissistic_number()