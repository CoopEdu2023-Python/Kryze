list = [1, 2.0, 3, 4.0, True, 'False']
for i in range(len(list)):
    if type(list[i]) == type(1) or type(list[i]) == type(1.1):
        list[i] *= 2
print(list)
