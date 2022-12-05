from sys import stdin
import heapq

N, M = map(int, input().split())
graph = dict()
for i in range(1, N+1):
    graph[i] = []

in_order = [0] * (N+1)
answer = []

for _ in range(M):
    A, B = map(int, stdin.readline().split())
    graph[A].append(B)
    in_order[B] += 1

heap = []
for i in range(1, N+1):
    if not in_order[i]:
        heap.append(i)

while heap:
    curr = heapq.heappop(heap)
    answer.append(curr)

    for next in graph[curr]:
        in_order[next] -= 1
        if not in_order[next]:
            heapq.heappush(heap, next)

print(*answer)
