def input_data():
    raw_str = input()
    nums = raw_str.split(",")
    nums[0] = int(nums[0])
    nums[1] = int(nums[1])
    return nums


def GCD(num_1, num_2):
    if num_2 == 0:
        return num_1
    else:
        return GCD(num_2, num_1 % num_2)


nums = input_data()
num_1 = nums[0]
num_2 = nums[1]
print(num_1 * num_2 // GCD(num_1, num_2))