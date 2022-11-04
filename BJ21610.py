dx, dy = [0, -1, -1, -1, 0, 1, 1, 1], [-1, -1, 0, 1, 1, 1, 0, -1]
cx, cy = [-1, -1, 1, 1], [-1, 1, -1, 1]

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]


def change(x, y):
    return (x+1)*1000 + (y+1)


def find(n):
    y = n % 1000 - 1
    x = (n-y-1)//1000-1
    return x, y


clouds = [[N-1, 0], [N-1, 1], [N-2, 0], [N-2, 1]]

for _ in range(M):
    d, s = map(int, input().split())
    temp = dict()

    for cloud in clouds:
        x = (cloud[0] + dx[d-1] * s) % N
        y = (cloud[1] + dy[d-1] * s) % N
        board[x][y] += 1
        temp[change(x, y)] = 0

    for n in temp.keys():
        x, y = find(n)

        for i in range(4):
            nx = x + cx[i]
            ny = y + cy[i]
            if 0 <= nx < N and 0 <= ny < N and board[nx][ny] > 0:
                temp[n] += 1

    clouds = []
    answer = 0
    for i in range(N):
        for j in range(N):
            if change(i, j) in temp.keys():
                board[i][j] += temp[change(i, j)]
            elif board[i][j] >= 2:
                clouds.append([i, j])
                board[i][j] -= 2
            answer += board[i][j]

print(answer)
