N = int(input())
data = [[] for _ in range(N)]

INF = 2147483647

for i in range(N):
    data[i] = list(map(int, input().split()))

dp = [[0 for _ in range(N)] for _ in range(N)]

for length in range(1, N):
    for start in range(N-length):
        dp[start][start+length] = INF
        for mid in range(start, start+length):
            dp[start][start+length] = min(dp[start][start+length], dp[start][mid] + dp[mid+1][start+length] + data[start][0] * data[mid][1] * data[start+length][1])

print(dp[0][-1])
