from sys import stdin

N = int(input())
ipt = [0] * (N+1)
dp = [0] * (N+1)

for i in range(1, N+1):
    ipt[i] = (int(stdin.readline()))

dp[1] = ipt[1]
if N > 1: dp[2] = ipt[1]+ipt[2]

for i in range(3, N+1):
    dp[i] = max(ipt[i]+dp[i-2], ipt[i]+dp[i-3]+ipt[i-1], dp[i-1])

print(max(dp))
