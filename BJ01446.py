N, D = map(int, input().split())
dp = [0] * (D+1)
for i in range(D+1): dp[i] = i

routes = []
for _ in range(N): routes.append(list(map(int, input().split())))
routes.sort()

for route in routes:
    start, end, l = route
    if l >= end-start: continue
    if end > D: continue

    dp[end] = min(dp[start]+l, dp[end])
    for j in range(end+1, D+1):
        dp[j] = min(dp[j-1]+1, dp[j])

print(dp[D])
