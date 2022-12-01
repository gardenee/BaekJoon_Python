from sys import stdin

dp = [[0, 0, 0], [1, 0, 0], [0, 1, 0], [1, 1, 1]]

for _ in range(int(input())):
    n = int(stdin.readline())

    for i in range(len(dp), n+1):
        dp.append([])
        dp[-1].append((dp[-2][1] + dp[-2][2]) % 1000000009)
        dp[-1].append((dp[-3][0] + dp[-3][2]) % 1000000009)
        dp[-1].append((dp[-4][0] + dp[-4][1]) % 1000000009)

    print(sum(dp[n]) % 1000000009)
