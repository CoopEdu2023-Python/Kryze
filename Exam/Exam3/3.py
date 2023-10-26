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
                # 跳过重复
                while num_list[left] == num_list[left + 1]:
                    left += 1
                while num_list[right] == num_list[right - 1]:
                    right -= 1
                left += 1
                right -= 1
            elif sum < 0:
                left += 1
            else:
                right -= 1
    return answers


num_list = [1, 1, 1, 1, -1, 0]
num_list.sort()
print(find_sum_of_3(num_list))