from collections import deque

M, N = map(int, input().split())
tomatoes = [list(map(int, input().split())) for _ in range(N)]

riped = 0
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
queue = deque()

for i in range(N):
    for j in range(M):
        if tomatoes[i][j] == 1:
            queue.append([0, i, j])
            riped += 1
        elif tomatoes[i][j] == -1:
            riped += 1

answer = 0
while queue:
    n, x, y = queue.popleft()

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < N and 0 <= ny < M and tomatoes[nx][ny] == 0:
            tomatoes[nx][ny] = n+1
            queue.append([n+1, nx, ny])
            riped += 1
            answer = max(answer, n+1)

if riped != N * M: answer = -1

print(answer)
