from sys import stdin

N, M = map(int, input().split())
kingdom = [[0] * (M+1)]
for _ in range(N):
    kingdom.append([0] + list(map(int, stdin.readline().split())))

for i in range(1, N+1):
    for j in range(1, M+1):
        kingdom[i][j] += kingdom[i][j-1] + kingdom[i-1][j] - kingdom[i-1][j-1]

K = int(input())
for _ in range(K):
    x1, y1, x2, y2 = map(int, stdin.readline().split())
    print(kingdom[x2][y2] - kingdom[x2][y1-1] - kingdom[x1-1][y2] + kingdom[x1-1][y1-1], end="\n")
