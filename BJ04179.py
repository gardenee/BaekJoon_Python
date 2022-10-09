R, C = map(int, input().split())
maze = [list(input()) for _ in range(R)]

fire = []
jh = []
for i in range(R):
    for j in range(C):
        if maze[i][j] == 'J':
            jh.append([i, j])
            maze[i][j] = 'x'
        elif maze[i][j] == 'F':
            fire.append([i, j])

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

t = 0
while jh:
    t += 1
    temp = []
    for f in fire:
        for n in range(4):
            nx = f[0] + dx[n]
            ny = f[1] + dy[n]
            if 0 <= nx < R and 0 <= ny < C and (maze[nx][ny] == '.' or maze[nx][ny] == 'x'):
                maze[nx][ny] = 'F'
                temp.append([nx, ny])

    fire = temp
    temp = []

    for curr in jh:
        for n in range(4):
            nx = curr[0] + dx[n]
            ny = curr[1] + dy[n]
            if 0 <= nx < R and 0 <= ny < C and maze[nx][ny] == '.':
                maze[nx][ny] = 'x'
                temp.append([nx, ny])
            if nx == -1 or ny == -1 or nx == R or ny == C:
                print(t)
                exit(0)
    jh = temp

print("IMPOSSIBLE")
