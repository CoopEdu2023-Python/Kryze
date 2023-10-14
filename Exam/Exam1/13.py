nums = [0, 1, 0, 3, 12]
for i in range(len(nums)):
    k = nums[nums.index(0)]
    for j in range(i + 1, len(nums)):
        if not nums[j] == 0:
            k = nums[i]
            nums[i] = nums[j]
            nums[j] = k
            break

print(nums)