def merge_dict(dict_1, dict_2):
    for key, value in dict_2.items():
        dict_1[key] = value


dict_1 = {1: 1, 2: 2}
dict_2 = {3: 3, 4: 4}
merge_dict(dict_1, dict_2)
print(dict_1)