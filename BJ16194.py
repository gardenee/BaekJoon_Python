N = int(input())
dp = [0] + list(map(int, input().split()))

for i in range(1, N+1):
    for j in range(1, i//2+1):
        dp[i] = min(dp[i], dp[j]+dp[i-j])

print(dp[N])
