from sys import stdin, setrecursionlimit
setrecursionlimit(10000000)

N, M, R = map(int, input().split())
graph = dict()

for _ in range(M):
    u, v = map(int, stdin.readline().split())
    graph.setdefault(u, [])
    graph.setdefault(v, [])
    graph[u].append(v)
    graph[v].append(u)

order = []
visited = [False] * (N+1)
visited[R] = True
graph.setdefault(R, [])


def dfs(curr):
    global order, visited
    order.append(curr)

    next_nodes = graph[curr]
    next_nodes.sort()

    for next in next_nodes:
        if not visited[next]:
            visited[next] = True
            dfs(next)


dfs(R)
answer = [0] * N

for i in range(len(order)):
    answer[order[i]-1] = i+1

for o in answer:
    print(o)
