import bisect

N = int(input())
lines = list()
for _ in range(N): lines.append(list(map(int, input().split())))
lines.sort()

dp = [lines[0][1]]
for i in range(N):
    if lines[i][1] > dp[-1]:
        dp.append(lines[i][1])
    else:
        idx = bisect.bisect_left(dp, lines[i][1])
        dp[idx] = lines[i][1]

print(N - len(dp))
