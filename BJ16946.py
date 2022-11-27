from collections import deque

N, M = map(int, input().split())
board = [list(input()) for _ in range(N)]
bfs_cnt = [board[i][:] for i in range(N)]

dx, dy = [0, 0, -1, 1], [-1, 1, 0, 0]
sequence = 1

for i in range(N):
    for j in range(M):
        if bfs_cnt[i][j] == "0":
            bfs_cnt[i][j] = 0
            temp = [[i, j]]
            queue = deque([[i, j]])
            while queue:
                x, y = queue.popleft()
                for n in range(4):
                    nx, ny = x + dx[n], y + dy[n]
                    if 0 <= nx < N and 0 <= ny < M and bfs_cnt[nx][ny] == "0":
                        bfs_cnt[nx][ny] = 0
                        temp.append([nx, ny])
                        queue.append([nx, ny])
            for t in temp:
                x, y = t
                bfs_cnt[x][y] = [sequence, len(temp)]
            sequence += 1

for i in range(N):
    for j in range(M):
        if board[i][j] == "1":
            temp = set()
            cnt = 0
            for n in range(4):
                nx, ny = i + dx[n], j + dy[n]
                if 0 <= nx < N and 0 <= ny < M and board[nx][ny] == "0":
                    if bfs_cnt[nx][ny][0] not in temp:
                        temp.add(bfs_cnt[nx][ny][0])
                        cnt += bfs_cnt[nx][ny][1]
            board[i][j] = (cnt+1) % 10
        print(board[i][j], end="")
    print()
