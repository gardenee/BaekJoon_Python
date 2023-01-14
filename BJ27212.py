N, M, C = map(int, input().split())
W = [list(map(int, input().split())) for _ in range(C)]

A = [0] + list(map(int, input().split()))
B = [0] + list(map(int, input().split()))

dp = [[0] * (M+1) for _ in range(N+1)]

for i in range(1, N+1):
    for j in range(1, M+1):
        dp[i][j] = max(max(dp[i-1][j-1] + W[A[i]-1][B[j]-1], dp[i][j-1]), dp[i-1][j])

print(dp[N][M])