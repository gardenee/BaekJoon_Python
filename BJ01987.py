R, C = map(int, input().split())
board = [list(input()) for _ in range(R)]

dx, dy = [0, 0, -1, 1], [-1, 1, 0, 0]
answer = 1


def dfs(position, visited):
    global answer
    x, y = position
    cnt = 0

    for n in range(4):
        nx, ny = x+dx[n], y+dy[n]
        if 0 <= nx < R and 0 <= ny < C and board[nx][ny] not in visited:
            char = board[nx][ny]
            visited.add(char)
            dfs([nx, ny], visited)
            visited.remove(char)
            cnt += 1

    if cnt == 0:
        answer = max(answer, len(visited))


dfs([0, 0], set([board[0][0]]))
print(answer)
