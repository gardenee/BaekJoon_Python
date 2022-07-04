from sys import stdin

graph = dict()
N = int(input())
M = int(input())

parents = []
for i in range(0, N+1): parents.append(i)

for _ in range(M):
    a, b, c = map(int, stdin.readline().split())
    graph.setdefault(c, list())
    graph[c].append([a, b])


def findparents(n):
    if parents[n] == n: return n
    else:
        parents[n] = findparents(parents[n])
        return parents[n]

def union(a, b):
    parents[findparents(a)] = parents[findparents(b)]


keys = list(graph.keys())
keys.sort()

cnt = 0
ans = 0
for key in keys:
    curr = graph[key]
    for c in curr:
        if findparents(c[0]) != findparents(c[1]):
            union(c[0], c[1])
            cnt += 1
            ans += key

print(ans)
