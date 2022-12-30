from sys import stdin
import heapq

V, E = map(int, input().split())
K = int(input())

INF = 300000 * 200000 + 1
graph = [[] for _ in range(V+1)]

for _ in range(E):
    u, v, w = map(int, stdin.readline().split())
    graph[u].append([v, w])

answer = [INF] * (V+1)
answer[K] = 0
heap = [[0, K]]

while heap:
    d, curr = heapq.heappop(heap)

    for next, w in graph[curr]:
        if answer[next] > w + d:
            answer[next] = w + d
            heapq.heappush(heap, [w+d, next])

for output in answer[1:]:
    if output == INF:
        print("INF")
    else:
        print(output)
