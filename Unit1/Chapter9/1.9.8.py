def plusOne(digits: list[int]) -> list[int]:
    return list(map(int, list(str(int("".join(map(str, digits))) + 1))))

print(plusOne([1, 2, 3]))

