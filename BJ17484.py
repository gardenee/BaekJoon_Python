N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

answer = 1000
dy = [-1, 0, 1]


def dfs(x, y, d, fuel):
    global answer

    if x == N-1:
        answer = min(answer, fuel)
        return

    for n in range(3):
        if n == d: continue
        ny = y + dy[n]
        if 0 <= ny < M: dfs(x+1, ny, n, fuel+board[x+1][ny])


for i in range(M):
    dfs(0, i, 3, board[0][i])

print(answer)
