N = int(input())
dp = [[0]*N for _ in range(N+1)]

for i in range(1, N+1):
    temp = list(map(int, input().split()))
    for j in range(i):
        if j == 0:
            dp[i][0] = dp[i-1][0] + temp[0]
        elif j == i-1:
            dp[i][j] = dp[i-1][j-1] + temp[j]
        else:
            dp[i][j] = max(dp[i-1][j-1], dp[i-1][j]) + temp[j]

print(max(dp[N]))
