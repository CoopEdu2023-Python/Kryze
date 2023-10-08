def mul(size):
    for i in range(1, size + 1):
        for j in range(1, i + 1):
            print(f"{j} * {i} = {j * i}", end="    ")
        print("\n")
mul(5)