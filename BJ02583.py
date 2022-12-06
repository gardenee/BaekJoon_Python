M, N, K = map(int, input().split())
board = [[0] * M for _ in range(N)]
answer = []

for _ in range(K):
    x1, y1, x2, y2 = map(int, input().split())
    for x in range(x1, x2):
        for y in range(y1, y2):
            board[x][y] = 1

dx, dy = [0, 0, -1, 1], [-1, 1, 0, 0]

for i in range(N):
    for j in range(M):
        if board[i][j] == 0:
            temp = 1
            board[i][j] = 1
            stack = [[i, j]]
            while stack:
                x, y = stack.pop()
                for n in range(4):
                    nx, ny = x+dx[n], y+dy[n]
                    if 0 <= nx < N and 0 <= ny < M and board[nx][ny] == 0:
                        temp += 1
                        board[nx][ny] = 1
                        stack.append([nx, ny])
            answer.append(temp)

answer.sort()
print(len(answer))
print(*answer)