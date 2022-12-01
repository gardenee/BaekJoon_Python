from collections import deque


def find_end(d, x, y):
    nx, ny = x + dx[d], y + dy[d]
    if board[nx][ny] == "#":
        return x, y
    if board[nx][ny] == "O":
        return nx, ny

    return find_end(d, nx, ny)


N, M = map(int, input().split())
board = [list(input()) for _ in range(N)]

queue = deque()
queue.append([""] * 5)

for i in range(N):
    for j in range(M):
        if board[i][j] == "R":
            queue[0][1] = i
            queue[0][2] = j
            board[i][j] = "."
        elif board[i][j] == "B":
            queue[0][3] = i
            queue[0][4] = j
            board[i][j] = "."

answer = -1
dx, dy = [0, 0, -1, 1], [-1, 1, 0, 0]

visited = set()

while queue:
    log, rx, ry, bx, by = queue.popleft()
    if len(log) == 10:
        break

    for n in range(4):
        rnx, rny = find_end(n, rx, ry)
        bnx, bny = find_end(n, bx, by)

        if rnx == bnx and rny == bny and board[rnx][rny] != "O":
            if n == 0:
                if ry > by:
                    rny += 1
                elif ry < by:
                    bny += 1
            elif n == 1:
                if ry > by:
                    bny -= 1
                elif ry < by:
                    rny -= 1
            elif n == 2:
                if rx > bx:
                    rnx += 1
                elif rx < bx:
                    bnx += 1
            elif n == 3:
                if rx > bx:
                    bnx -= 1
                elif rx < bx:
                    rnx -= 1

        if board[bnx][bny] == "O":
            continue
        elif board[rnx][rny] == "O":
            answer = len(log)+1
            queue = []
            break

        if bnx == bx and bny == by and rnx == rx and rny == ry:
            continue

        if log+str(n) not in visited:
            queue.append([log + str(n), rnx, rny, bnx, bny])
            visited.add(log + str(n))

print(answer)
