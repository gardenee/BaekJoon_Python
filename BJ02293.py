n, k = map(int, input().split())
coin = []
for _ in range(n):
    coin.append(int(input()))

dp = [0] * (k+1)

for i in range(k+1):
    if i % coin[0] == 0:
        dp[i] = 1

for i in range(1, n):
    for j in range(1, k+1):
        if j >= coin[i]:
            dp[j] += dp[j-coin[i]]

print(dp[-1])
