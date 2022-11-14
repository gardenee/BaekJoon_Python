N, L, R = map(int, input().split())
land = [list(map(int, input().split())) for _ in range(N)]

dx, dy = [0, 0, -1, 1], [-1, 1, 0, 0]
answer, changed = 0, True

while changed:
    visited = [[False] * N for _ in range(N)]
    changed = False

    for x in range(N):
        for y in range(N):
            if not visited[x][y]:
                merge = [[x, y]]
                visited[x][y] = True
                total = land[x][y]

                stack = [[x, y]]
                while stack:
                    i, j = stack.pop()

                    for n in range(4):
                        nx, ny = i+dx[n], j+dy[n]
                        if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny] and L <= abs(land[i][j]-land[nx][ny]) <= R:
                            total += land[nx][ny]
                            visited[nx][ny] = True
                            merge.append([nx, ny])
                            stack.append([nx, ny])

                total //= len(merge)
                for kingdom in merge:
                    i, j = kingdom
                    if land[i][j] != total:
                        changed = True
                    land[i][j] = total

    if changed:
        answer += 1

print(answer)
