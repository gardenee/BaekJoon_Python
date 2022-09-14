N, M = map(int, input().split())
memory = list(map(int, input().split()))
cost = list(map(int, input().split()))

dp = [[0] * 10001 for _ in range(N+1)]

for i in range(N):
    for j in range(1, 10001):
        if j < cost[i]:
            dp[i+1][j] = dp[i][j]
        else:
            dp[i+1][j] = max(dp[i][j], dp[i][j-cost[i]]+memory[i])
    print(dp[i+1])

for i in range(10001):
    if dp[-1][i] >= M:
        print(i)
        break
