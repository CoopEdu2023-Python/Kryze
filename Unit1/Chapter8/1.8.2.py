def check_subset(setSmall, setBig):
    return setSmall.issubset(setBig)


set1 = {1, 2}
set2 = {1, 2, 3}
print(check_subset(set1, set2))