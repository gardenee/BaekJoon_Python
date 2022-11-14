from collections import deque

n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

answer = [[-1] * m for _ in range(n)]
queue = deque()

for i in range(n):
    for j in range(m):
        if board[i][j] == 2:
            answer[i][j] = 0
            queue.append([i, j, 0])
        elif board[i][j] == 0:
            answer[i][j] = 0

dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

while queue:
    x, y, val = queue.popleft()
    for i in range(4):
        nx, ny = x+dx[i], y+dy[i]
        if 0 <= nx < n and 0 <= ny < m and board[nx][ny] == 1:
            answer[nx][ny] = val+1
            board[nx][ny] = 0
            queue.append([nx, ny, val+1])


for i in range(n):
    for j in range(m):
        print(answer[i][j], end=" ")
    print()
