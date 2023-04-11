N = int(input())
dp = [[1] * 10] + [[0] * 10 for _ in range(N+1)]

for i in range(1, N+1):
    dp[i][0] = 1
    for j in range(1, 10):
        dp[i][j] = (dp[i][j-1] + dp[i-1][j]) % 10007

print(dp[N][9] % 10007)