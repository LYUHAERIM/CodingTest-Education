nums = [1, 2, 3, 4, 5, 6]


resultSum = 0
# sum
for num in nums:
    resultSum += num

# max
resultMax = nums[0]
for num in nums:
    if resultMax < num:
        resultMax = num

# reverse
resultReverse = []
for i in range(len(nums)):
    resultReverse.append(nums[len(nums) - 1 - i])

print("sum:", resultSum)
print("max:", resultMax)
print("reverse:", resultReverse)
