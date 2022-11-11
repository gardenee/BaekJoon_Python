from collections import deque

N, M = map(int, input().split())
board = [list(input()) for _ in range(N)]
visited = [[[False, False] for _ in range(M)] for _ in range(N)]

dx, dy = [0, 0, -1, 1], [-1, 1, 0, 0]

answer = -1
visited[0][0][0] = True
queue = deque([[0, 0, 1, True]])

while queue:
    curr = queue.popleft()
    x, y, d, can_break = curr
    if x == N-1 and y == M-1:
        answer = d
        break

    for n in range(4):
        nx, ny = x+dx[n], y+dy[n]
        if 0 <= nx < N and 0 <= ny < M:
            if board[nx][ny] == '0':
                if can_break and not visited[nx][ny][0]:
                    visited[nx][ny][0] = True
                    queue.append([nx, ny, d+1, can_break])
                elif not can_break and not visited[nx][ny][1]:
                    visited[nx][ny][1] = True
                    queue.append([nx, ny, d+1, can_break])
            elif can_break and board[nx][ny] == '1' and not visited[nx][ny][1]:
                visited[nx][ny][1] = True
                queue.append([nx, ny, d+1, False])

print(answer)
