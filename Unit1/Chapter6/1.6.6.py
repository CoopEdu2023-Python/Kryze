def mul(size):
    rt = ""
    for i in range(1, size + 1):
        for j in range(1, i + 1):
            rt += f"{j} * {i} = {j * i}" + "    "
            # print(f"{j} * {i} = {j * i}", end="    ")
        # print("\n")
        rt += "\n"
    return rt
print(mul(5))