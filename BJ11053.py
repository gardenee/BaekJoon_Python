n = int(input())
lst = list(map(int, input().split()))
dp = [0] * 1001

for i in lst:
    dp[i] = 1 + max(dp[:i])

print(max(dp))
