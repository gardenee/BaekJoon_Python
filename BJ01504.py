from sys import stdin
from collections import deque

N, E = map(int, input().split())
graph = [dict() for _ in range(N+1)]

INF = 1000000000

for _ in range(E):
    a, b, c = map(int, stdin.readline().split())
    graph[a][b] = c
    graph[b][a] = c

v1, v2 = map(int, input().split())

distance = [[INF] * 4 for _ in range(N+1)]
distance[1][0] = 0

queue = deque([[1, 0, 0]])

if v1 == 1:
    queue[0][2] = 1
    distance[1][1] = 0

while queue:
    node, d, idx = queue.popleft()

    for next_node in graph[node].keys():
        l = graph[node][next_node]
        curr_idx = idx

        if curr_idx == 0 and next_node == v1:
            curr_idx = 1
        elif curr_idx == 0 and next_node == v2:
            curr_idx = 2
        elif (curr_idx == 1 and next_node == v2) or (curr_idx == 2 and next_node == v1):
            curr_idx = 3

        if d + l < distance[next_node][curr_idx]:
            distance[next_node][curr_idx] = d + l
            queue.append([next_node, d + l, curr_idx])

if distance[N][3] != INF:
    print(distance[N][3])
else:
    print(-1)
