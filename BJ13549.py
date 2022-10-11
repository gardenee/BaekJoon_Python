import heapq

N, K = map(int, input().split())
INF = 200001
dp = [INF] * INF
visited = [False] * INF

dp[K] = 0
heap = []
heapq.heappush(heap, (0, K))

while heap:
    curr = heapq.heappop(heap)
    n, cnt = curr[1], curr[0]

    if n == N:
        break

    if visited[n]: continue
    else: visited[n] = True

    if n+1 < INF and not visited[n+1] and dp[n+1] > cnt+1:
        dp[n+1] = cnt+1
        heapq.heappush(heap, (cnt+1, n+1))
    if not visited[n-1] and dp[n-1] > cnt+1:
        dp[n-1] = cnt+1
        heapq.heappush(heap, (cnt+1, n-1))
    if n % 2 == 0 and not visited[n//2] and dp[n//2] > cnt:
        dp[n//2] = cnt
        heapq.heappush(heap, (cnt, n//2))

print(dp[N])
