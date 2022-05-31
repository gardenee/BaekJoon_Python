X = int(input())
dp = [1000001] * (X+1)
dp[0] = 0
dp[1] = 0

for i in range(2, X+1):
    if i % 3 == 0: dp[i] = dp[i//3]+1
    if i % 2 == 0: dp[i] = min(dp[i//2]+1, dp[i])
    dp[i] = min(dp[i-1]+1, dp[i])

print(dp[X])
