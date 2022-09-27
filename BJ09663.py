def dfs(n, i, j, board):
    global answer
    if n == 0:
        answer += 1
        return

    for x in range(N):
        if x < i or 1 in board[x]:
            continue
        for y in range(N):
            if x == i and y < j:
                continue
            if board[x][y] == 1:
                continue
            flag = True
            for a in range(8):
                m = 1
                while True:
                    nx = x + m * dx[a]
                    ny = y + m * dy[a]
                    if not (0 <= nx < N and 0 <= ny < N):
                        break
                    if board[nx][ny] == 1:
                        flag = False
                        break
                    m += 1
                if not flag:
                    break
            if flag:
                board[x][y] = 1
                dfs(n-1, x, y, board)
                board[x][y] = 0


N = int(input())
answer = 0
dx = [-1, -1, -1, 0, 0, 1, 1, 1]
dy = [-1, 0, 1, -1, 1, -1, 0, 1]

dfs(N, 0, 0, [[0]*N for _ in range(N)])
print(answer)
