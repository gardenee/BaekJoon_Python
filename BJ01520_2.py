M, N = map(int, input().split())
map = [list(map(int, input().split())) for _ in range(M)]
answer = 0

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
stack = [[0, 0]]

while stack:
    curr = stack.pop()
    x, y = curr[0], curr[1]

    for n in range(4):
        nx = x + dx[n]
        ny = y + dy[n]

        if nx == M-1 and ny == N-1:
            answer += 1
        elif 0 <= nx < M and 0 <= ny < N and map[x][y] > map[nx][ny]:
            stack.append([nx, ny])

print(answer)
