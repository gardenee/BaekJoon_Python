n, k = map(int, input().split())
money = set()
INF = 10001

for _ in range(n):
    money.add(int(input()))

money = list(money)
money.sort(reverse=True)
dp = [0] + [INF] * (k+1)

for m in money:
    if m > k:
        continue

    for i in range(m, k+1):
        if dp[i-m] != INF:
            dp[i] = min(dp[i], dp[i-m]+1)

if dp[k] == INF:
    dp[k] = -1

print(dp[k])
