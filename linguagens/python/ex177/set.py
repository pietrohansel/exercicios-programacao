
nums = [1, 2, 4, 2, 6]
nums_set = set(nums)

for i in range(1, len(nums) + 1):
    if i not in nums_set:
        print(i)