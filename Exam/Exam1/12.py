n = int(input("输入元素个数"))
nums = []
for i in range(n):
    nums.append(int(input("输入元素")))
print(nums)
for i in range(nums.count(0)):
    nums.append(nums.pop(nums.index(0)))
print(nums)