from collections import deque

dx, dy = [-2, -2, -1, -1, 1, 1, 2, 2], [1, -1, 2, -2, 2, -2, 1, -1]

for _ in range(int(input())):
    l = int(input())
    board = [[-1] * l for _ in range(l)]

    startX, startY = map(int, input().split())
    goalX, goalY = map(int, input().split())

    board[startX][startY] = 0
    queue = deque([[startX, startY]])

    while queue:
        x, y = queue.popleft()

        if x == goalX and y == goalY:
            print(board[x][y])
            break

        for n in range(8):
            nx, ny = x + dx[n], y + dy[n]

            if 0 <= nx < l and 0 <= ny < l and board[nx][ny] == -1:
                board[nx][ny] = board[x][y] + 1
                queue.append([nx, ny])
