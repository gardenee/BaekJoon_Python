N, K = map(int, input().split())
backpack = [[0, 0]]
dp = [[0] * (K+1) for _ in range(N+1)]

for _ in range(N):
    backpack.append(list(map(int, input().split())))

for i in range(1, N+1):
    for j in range(1, K+1):
        W = backpack[i][0]
        V = backpack[i][1]

        if j < W:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-W] + V)

print(dp[N][K])
