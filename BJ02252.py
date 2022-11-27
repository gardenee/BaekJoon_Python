from sys import stdin
from collections import deque

N, M = map(int, input().split())
graph = dict()
in_degree = [0] * (N+1)

for _ in range(M):
    A, B = map(int, stdin.readline().split())
    in_degree[B] += 1
    graph.setdefault(A, [])
    graph[A].append(B)

queue = deque()
for i in range(1, N+1):
    if not in_degree[i]:
        queue.append(i)

answer = []
while queue:
    curr = queue.popleft()
    answer.append(curr)

    if curr in graph:
        for next in graph[curr]:
            in_degree[next] -= 1
            if not in_degree[next]:
                queue.append(next)

print(*answer)
