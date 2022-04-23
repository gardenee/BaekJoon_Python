from sys import stdin
N = int(input())
prize = []

for _ in range(N):
    nums = list(map(int, stdin.readline().split()))
    nums.sort()
    if nums.count(nums[-1]) == 4:
        prize.append(nums[-1] * 5000 + 50000)
    elif nums.count(nums[-1]) == 3:
        prize.append(nums[-1] * 1000 + 10000)
    elif nums.count(nums[0]) == 3:
        prize.append(nums[0] * 1000 + 10000)
    elif len(set(nums)) == len(nums):
        prize.append(max(nums) * 100)
    elif nums.count(nums[0]) == 2 and nums.count(nums[-1]) == 2:
        prize.append(nums[0] * 500 + nums[-1] * 500 + 2000)
    else:
        x = 0
        for i in range(3):
            if nums[i] == nums[i+1]:
                x = nums[i]
                break
        prize.append(x * 100 + 1000)

print(max(prize))
