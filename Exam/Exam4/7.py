k = int(input())
raw_str = input()
nums = raw_str.split(",")
for i in range(len(nums)):
    nums[i] = int(nums[i])

for i in range(k):
    nums.insert(0, nums.pop(-1))

print(nums)
