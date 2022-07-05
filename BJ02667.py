N = int(input())
graph = []

for _ in range(N):
    graph.append(list(input()))

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
visited = [[False] * N for _ in range(N)]
answer = list()


def dfs(dot):
    global visited
    global temp
    y = dot[0]
    x = dot[1]

    for n in range(4):
        nx = x + dx[n]
        ny = y + dy[n]
        if 0 <= nx < N and 0 <= ny < N:
            if (not visited[ny][nx]) and graph[ny][nx] == "1":
                visited[ny][nx] = True
                temp += 1
                dfs([ny, nx])


for i in range(N):
    for j in range(N):
        if graph[i][j] == "1" and not visited[i][j]:
            visited[i][j] = True
            temp = 1
            dfs([i, j])
            answer.append(temp)

answer.sort()

print(len(answer))
for ans in answer: print(ans)
