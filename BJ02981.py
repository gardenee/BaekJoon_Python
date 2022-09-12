N = int(input())
nums = []

for _ in range(N):
    nums.append(int(input()))
nums.sort()

for i in range(2, nums[0]+1):
    mod = 