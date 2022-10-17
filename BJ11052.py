N = int(input())
P = list(map(int, input().split()))
dp = [0] * (N+1)
answer = 0

for i in range(1, N+1):
    dp[i] = P[i-1]
    for j in range(1, (i+1)//2+1):
        dp[i] = max(dp[i], dp[j]+dp[i-j])
    answer = max(answer, dp[i])

print(answer)
