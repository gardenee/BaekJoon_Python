n = int(input())
nums = list(map(int, input().split()))
nums.sort()
dif = []
for i in range(len(nums)-1):
    dif.append(nums[i+1] - nums[i])
ans = 0
for i in range(1, n):
    ans += 2 * i * (n-i) * dif[i-1]

print(ans)
