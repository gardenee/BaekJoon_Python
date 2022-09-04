import bisect

N = int(input())
ipt = list(map(int, input().split()))

dp = [1] * (N+1)
asc = [ipt[0]]
desc = [ipt[-1]]
answer = 1

for i in range(N):
    if ipt[i] > asc[-1]:
        asc.append(ipt[i])
        dp[i] = len(asc)
    else:
        idx = bisect.bisect_left(asc, ipt[i])
        asc[idx] = ipt[i]
        dp[i] = idx + 1

for i in range(N-1, -1, -1):
    if ipt[i] > desc[-1]:
        desc.append(ipt[i])
        dp[i] += len(desc)
    else:
        idx = bisect.bisect_left(desc, ipt[i])
        desc[idx] = ipt[i]
        dp[i] += idx + 1

print(max(dp)-1)
