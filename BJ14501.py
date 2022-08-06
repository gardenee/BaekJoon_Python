N = int(input())
ipt = []

for _ in range(N):
    ipt.append(list(map(int, input().split())))

dp = [0] * N
for i in range(N):
    for j in range(i):
        if (ipt[j][0] + j - 1) < i:
            dp[i] = max(dp[i], dp[j])
    if (ipt[i][0] + i) <= N:
        dp[i] += ipt[i][1]

print(max(dp))
