from collections import deque

N, M = map(int, input().split())
dx = [-1, -1, -1, 0, 0, 1, 1, 1]
dy = [-1, 0, 1, -1, 1, -1, 0, 1]

graph = [list(map(int, input().split())) for _ in range(N)]
answer = 0

for i in range(N):
    for j in range(M):
        if graph[i][j] == 0:
            visited = [[False for _ in range(M)] for _ in range(N)]
            visited[i][j] = True
            cnt = 0

            queue = deque([[i, j, 0]])
            while queue and cnt == 0:
                curr = queue.popleft()
                d = curr[2]
                for n in range(8):
                    y = curr[0] + dy[n]
                    x = curr[1] + dx[n]
                    if 0 <= x < M and 0 <= y < N and not visited[y][x]:
                        if graph[y][x] == 0:
                            visited[y][x] = True
                            queue.append([y, x, d+1])
                        else:
                            cnt = d+1
                            break
            answer = max(answer, cnt)

print(answer)
