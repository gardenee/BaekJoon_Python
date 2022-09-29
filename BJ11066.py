T = int(input())
ref = [1]
for _ in range(10):
    ref.append(ref[-1] * 2)

for _ in range(T):
    K = int(input())
    data = list(map(int, input().split()))

    dp = [[0] * K for _ in range(K)]
    for i in range(K-1):
        dp[i][i+1] = data[i] + data[i+1]
        for j in range(i+2, K):
            dp[i][j] = dp[i][j-1] + data[j]

    for j in range(2, K):
        for i in range(j-2, -1, -1):
            dp[i][j] += min((dp[i][i+k] + dp[i+1+k][j]) for k in range(j-i))

    print(dp[0][K-1])
