# 길이 m 짜리 리스트에서
# 길이 n 짜리 구간의 합을 구하시오

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# n = int(input())
n = 3
result1 = []
result2 = []
result3 = []

# (1)
for i in range(len(nums) - n + 1):
    tmp = 0
    for j in range(n):
        tmp += nums[i + j]
    result1.append(tmp)

print(result1)

# (2)
for i in range(len(nums) - n + 1):
    result2.append(sum(nums[i : i + n]))

print(result2)


# (3)
def cumsum(lst, n):
    return [sum(lst[i : i + n]) for i in range(len(lst) - n + 1)]


print(cumsum(nums, n))

# (4)
base_case = sum(nums[:n])
result3.append(base_case)

for i in range(len(nums) - n):  # 이미 base_case에 한번 넣었기 때문에
    base_case = base_case - nums[i] + nums[i + n]
    result3.append(result3[-1] - nums[i] + nums[i + n])
print(result3)
