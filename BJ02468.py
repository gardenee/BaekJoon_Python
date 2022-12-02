N = int(input())
land = [list(map(int, input().split())) for _ in range(N)]

dx, dy = [0, 0, -1, 1], [-1, 1, 0, 0]

answer = 0
for n in range(101):
    safe_land = 0
    visited = [[False] * N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if land[i][j] > n and not visited[i][j]:
                visited[i][j] = True
                safe_land += 1
                stack = [[i, j]]
                while stack:
                    x, y = stack.pop()
                    for m in range(4):
                        nx, ny = x + dx[m], y + dy[m]
                        if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny] and land[nx][ny] > n:
                            visited[nx][ny] = True
                            stack.append([nx, ny])

    answer = max(answer, safe_land)

print(answer)
