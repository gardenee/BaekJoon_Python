import sys
sys.setrecursionlimit(10 ** 8)

M, N = map(int, input().split())
map = [list(map(int, input().split())) for _ in range(M)]
dp = [[-1] * N for _ in range(M)]

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]


def dfs(x, y):
    if x == M-1 and y == N-1:
        return 1
    if dp[x][y] != -1:
        return dp[x][y]

    dp[x][y] = 0

    for n in range(4):
        nx = x + dx[n]
        ny = y + dy[n]
        if 0 <= nx < M and 0 <= ny < N and map[x][y] > map[nx][ny]:
            dp[x][y] += dfs(nx, ny)

    return dp[x][y]


print(dfs(0, 0))
