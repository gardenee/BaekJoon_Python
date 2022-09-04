import bisect

N = int(input())
ipt = list(map(int, input().split()))
dp = [ipt[0]]

for i in range(N):
    if ipt[i] > dp[-1]:
        dp.append(ipt[i])
    else:
        idx = bisect.bisect_left(dp, ipt[i])
        dp[idx] = ipt[i]

print(len(dp))
