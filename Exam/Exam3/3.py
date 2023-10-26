def find_sum_of_3(num_list: list) -> list[tuple]:
    answers = []
    for i in range(len(num_list) - 2):
        right = len(num_list) - 1
        left = i + 1
        if num_list[i] == num_list[i - 1] and i > 0:
            continue
        while left < right:
            sum = num_list[i] + num_list[left] + num_list[right]
            if sum == 0:
                answers.append(tuple(sorted([num_list[i], num_list[left], num_list[right]])))
                left += 1
                right -= 1
            elif sum < 0:
                left += 1
            else:
                right -= 1
    return answers


num_list = [-1, 0, 1, 2, -1, -4, 0, 2, 0, 4, -4, -2, -1, 2]
num_list.sort()
print(list(set(find_sum_of_3(num_list))))