def max_product(num_list: list) -> int:
    num_list.sort()
    minimums = num_list[0] * num_list[1] * num_list[-1]
    maximums = num_list[-1] * num_list[-2] * num_list[-3]
    return max(minimums, maximums)


input_nums = [1, 11, -9, -8, -1, 10]
print(max_product(input_nums))
