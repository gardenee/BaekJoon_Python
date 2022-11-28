from collections import deque

N = int(input())
graph = dict()
for i in range(N):
    graph[i] = []

for i in range(N):
    ipt = list(map(int, input().split()))
    for j in range(N):
        if ipt[j] == 1:
            graph[i].append(j)

answer = [[0] * N for _ in range(N)]

for i in range(N):
    queue = deque(graph[i])
    while queue:
        curr = queue.popleft()
        if answer[i][curr]:
            continue

        answer[i][curr] = 1
        for temp in graph[curr]:
            if not answer[i][temp]:
                queue.append(temp)

    print(*answer[i])
