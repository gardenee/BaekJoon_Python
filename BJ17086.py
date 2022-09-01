N, M = map(int, input().split())

graph = []

for _ in range(N):
    graph.append(list(map(int, input().split())))

answer = 0
for i in range(N):
    for j in range(M):
        if graph[i][j] == 0:
            flag = True
            n = 0

            while flag:
                n += 1
                maxX = min(j+n, M-1)
                minX = max(0, j-n)
                maxY = min(i+n, N-1)
                minY = max(0, i-n)

                if minY == i-n:
                    for x in range(minX, maxX+1):
                        if graph[minY][x] == 1:
                            flag = False
                            break
                if maxY == i+n:
                    for x in range(minX, maxX+1):
                        if graph[maxY][x] == 1:
                            flag = False
                            break
                if minX == j-n:
                    for y in range(minY, maxY+1):
                        if graph[y][minX] == 1:
                            flag = False
                            break
                if maxX == j+n:
                    for y in range(minY, maxY+1):
                        if graph[y][maxX] == 1:
                            flag = False
                            break

            answer = max(answer, n)

print(answer)
