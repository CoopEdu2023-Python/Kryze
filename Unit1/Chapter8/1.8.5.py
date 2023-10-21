def is_exist(target, value):
    for i in target:
        if value == i:
            return True
    else:
        return False


my_set = {1, 4, 7, 2, 6}
value_exist = 7
value_not_exist = 0
print(is_exist(my_set, value_exist))
print(is_exist(my_set, value_not_exist))