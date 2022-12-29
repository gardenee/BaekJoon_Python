N = int(input())
dp = [0] * max(6, N+1)

dp[3], dp[5] = 1, 1

for n in range(6, N+1):
    if dp[n-3]:
        dp[n] = dp[n-3] + 1

    if dp[n-5]:
        if dp[n-3]:
            dp[n] = min(dp[n], dp[n-5] + 1)
        else:
            dp[n] = dp[n-5] + 1

print(dp[N]) if dp[N] else print(-1)
