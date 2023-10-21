dictionary_of_number = dict()
for i in range(1, 16):
    dictionary_of_number[i] = i * i
for key, value in dictionary_of_number.items():
    print(f"{key} :{value}")