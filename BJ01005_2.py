from sys import stdin

T = int(input())
for _ in range(T):
    N, K = map(int, stdin.readline().split())
    time = list(map(int, input().split()))

    graph = dict()
    for _ in range(K):
        x, y = map(int, input().split())
        graph.setdefault(y, [])
        graph[y].append(x)

    W = int(input())
    dp = [0] * N
    dp[W-1] = time[W-1]

    son = [W]
    while son:
        temp = set()
        for s in son:
            if graph.get(s):
                for p in graph[s]:
                    temp.add(p)
                    dp[p-1] = max(dp[s-1]+time[p-1], dp[p-1])

        son = list(temp)

    print(max(dp))
