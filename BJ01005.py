T = int(input())
for _ in range(T):
    N, K = map(int, input().split())
    time = [0] + list(map(int, input().split()))

    graph = dict()
    for _ in range(K):
        x, y = map(int, input().split())
        graph.setdefault(y, [])
        graph[y].append(x)

    W = int(input())
    depth = [-1] * (N+1)
    depth[W] = 0
    if graph.get(W):
        curr = graph[W]

    i = 0
    while curr:
        i += 1
        temp = []
        for c in curr:
            depth[c] = i
            if graph.get(c):
                temp += graph[c]
        curr = temp

    calculate = [0] * (N+1)
    for i in range(N+1):
        d = depth[i]
        if d > -1:
            calculate[d] = max(calculate[d], time[i])

    print(sum(calculate))
