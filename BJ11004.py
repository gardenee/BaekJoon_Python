import heapq

N, K = map(int, input().split())
nums = list(map(int, input().rstrip().split()))
heap = []

for n in nums:
    if len(heap) < K:
        heapq.heappush(heap, -n)
    else:
        heapq.heappushpop(heap, -n)

print(-1 * heapq.heappop(heap))
