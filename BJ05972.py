from sys import stdin
import heapq

N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]

for _ in range(M):
    A, B, C = map(int, stdin.readline().split())
    graph[A].append([B, C])
    graph[B].append([A, C])


INF = 1000 * M
dp = [INF] * (N+1)
dp[1] = 0
heap = [[0, 1]]


while heap:
    price, curr = heapq.heappop(heap)
    if curr == N: break
    if dp[curr] < price: continue

    nodes = graph[curr]
    for node in nodes:
        n, v = node
        if price+v < dp[n]:
            dp[n] = price+v
            heapq.heappush(heap, [dp[n], n])

print(dp[N])
