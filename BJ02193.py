N = int(input())
dp = [0] * (N+2)
dp[1] = 1
dp[2] = 1

for i in range(3, N+1):
    dp[i] = dp[i-1] + dp[i-2]

print(dp[N])
