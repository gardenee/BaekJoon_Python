from sys import stdin

N, M = map(int, input().split())
graph = dict()
for i in range(1, N+1):
    graph[i] = []

for _ in range(M):
    u, v = map(int, stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)

answer = 0
visited = [False] * (N+1)

for i in range(1, N+1):
    if not visited[i]:
        answer += 1
        visited[i] = True
        stack = [i]

        while stack:
            curr = stack.pop()
            for node in graph[curr]:
                if not visited[node]:
                    visited[node] = True
                    stack.append(node)

print(answer)
