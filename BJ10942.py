from sys import stdin

N = int(input())
nums = list(map(int, input().split()))
M = int(input())

dp = [[0] * (N+1) for _ in range(N+1)]

for i in range(1, N+1):
    dp[i][i] = 1
    if i < N and nums[i-1] == nums[i]:
        dp[i][i+1] = 1

for j in range(1, N+1):
    for i in range(1, N+1):
        if i < N and nums[i-1] == nums[j-1] and dp[i+1][j-1] == 1:
            dp[i][j] = 1

for _ in range(M):
    S, E = map(int, stdin.readline().split())
    print(dp[S][E])
