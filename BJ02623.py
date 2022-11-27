from collections import deque

N, M = map(int, input().split())

graph = dict()
in_order = [0] * (N+1)

for _ in range(M):
    orders = list(map(int, input().split()))
    for i in range(2, len(orders)):
        B = orders[i]
        for j in range(1, i):
            A = orders[j]
            graph.setdefault(A, set())
            if B not in graph[A]:
                in_order[B] += 1
            graph[A].add(B)

queue = deque()
for i in range(1, N+1):
    if not in_order[i]:
        queue.append(i)

answer = []
while queue:
    curr = queue.popleft()
    answer.append(curr)

    if curr in graph:
        for next in graph[curr]:
            if not in_order[next]:
                queue = []
                break
            in_order[next] -= 1
            if not in_order[next]:
                queue.append(next)

if len(answer) == N:
    for i in range(N):
        print(answer[i])
else:
    print(0)
