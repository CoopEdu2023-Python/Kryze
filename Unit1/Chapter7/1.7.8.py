def sortlist(list):
    mid = list
    mid.sort()
    return mid
list = [1, 5, 2, 4, 9]
print(f"old:{list}")
print(f"new:{sortlist(list)}")