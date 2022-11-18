from collections import deque

M, N, H = map(int, input().split())
box = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]
dx, dy, dz = [0, 0, 0, 0, -1, 1], [0, 0, -1, 1, 0, 0], [-1, 1, 0, 0, 0, 0]

answer, fresh = 0, 0
queue = deque()
for x in range(H):
    for y in range(N):
        for z in range(M):
            if box[x][y][z] == 1:
                queue.append([x, y, z, 1])
            elif box[x][y][z] == 0:
                fresh += 1

while queue:
    x, y, z, d = queue.popleft()
    for n in range(6):
        nx = x + dx[n]
        ny = y + dy[n]
        nz = z + dz[n]
        if 0 <= nx < H and 0 <= ny < N and 0 <= nz < M and box[nx][ny][nz] == 0:
            answer = max(answer, d)
            box[nx][ny][nz] = 1
            queue.append([nx, ny, nz, d+1])
            fresh -= 1

if fresh:
    print(-1)
else:
    print(answer)
