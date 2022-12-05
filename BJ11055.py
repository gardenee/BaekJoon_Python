N = int(input())
lst = [0] + list(map(int, input().split()))
dp = [0] * (N+1)

for i in range(1, N+1):
    sum = 0
    for j in range(i):
        if lst[j] < lst[i] and dp[j] > sum:
            sum = dp[j]
    dp[i] = sum + lst[i]

print(max(dp))
