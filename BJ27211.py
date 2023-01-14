N, M = map(int, input().split())
world_map = [list(map(int, input().split())) for _ in range(N)]

dx, dy = [0, 0, -1, 1], [-1, 1, 0, 0]
answer = 0

for i in range(N):
    for j in range(M):
        if world_map[i][j]:
            continue

        answer += 1
        stack = [[i, j]]

        while stack:
            x, y = stack.pop()

            for n in range(4):
                nx = (x + dx[n]) % N
                ny = (y + dy[n]) % M

                if not world_map[nx][ny]:
                    stack.append([nx, ny])
                    world_map[nx][ny] = 1

print(answer)