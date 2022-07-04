import sys
sys.setrecursionlimit(200000)

while(True):
    m, n = map(int, input().split())
    if m == n == 0: break

    parents = []
    for i in range(m+1): parents.append(i)
    graph = dict()

    sum = 0
    for _ in range(n):
        a, b, c = map(int, sys.stdin.readline().split())
        sum += c
        graph.setdefault(c, list())
        graph[c].append([a, b])


    def findparents(n):
        if n == parents[n]: return n
        else:
            parents[n] = findparents(parents[n])
            return parents[n]

    def union(a, b):
        parents[findparents(a)] = parents[findparents(b)]


    keys = list(graph.keys())
    keys.sort()
    cnt = 0

    for key in keys:
        curr = graph[key]
        for c in curr:
            if findparents(c[0]) != findparents(c[1]):
                union(c[0], c[1])
                sum -= key
                cnt += 1
        if cnt == m-1: break

    print(sum)
