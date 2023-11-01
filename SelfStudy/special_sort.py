num_list = []
raw_input = input()
num_list.extend(raw_input.split(" "))
num = len(num_list)
for i in range(num):
    num_list[i] = int(num_list[i])

for i in range(num):
    for j in range(i + 1, num):
        if num_list[i] < num_list[j]:
            _mid = num_list[i]
            num_list[i] = num_list[j]
            num_list[j] = _mid

part_1 = num_list[:num // 2]
part_2 = num_list[:num // 2 - 1:-1]
for i in part_1:
    print(i, end=" ")
for i in part_2:
    print(i, end=" ")

# 1 2 3 4 5 6 7 8
# 1 4 67 3 2 6
# 3 3 3 3 3 2 2