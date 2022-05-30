import sys


def search(n: int, m: int):
    if graph[n][m] == 0:
        return 0

    graph[n][m] = 0
    stack = []
    stack.append((n,m))
    while (stack):
        curr = stack.pop()
        dx = [1, -1, 0, 0]
        dy = [0, 0, 1, -1]
        for i in range(4):
            x = curr[1] + dx[i]
            y = curr[0] + dy[i]
            if 0 <= x < M and 0 <= y < N and graph[y][x] == 1:
                graph[y][x] = 0
                stack.append((y,x))
    return 1


for _ in range(int(input())):
    M, N, K = map(int, sys.stdin.readline().split())
    graph = [[0] * M for _ in range(N)]

    for _ in range(K):
        m, n = map(int, sys.stdin.readline().split())
        graph[n][m] = 1

    ans = 0
    for i in range(N):
        for j in range(M):
            ans += search(i, j)

    print(ans)
