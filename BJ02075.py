import heapq
from sys import stdin

N = int(input())
heap = []

for _ in range(N):
    curr = list(map(int, stdin.readline().rstrip().split()))
    for c in curr:
        if len(heap) >= N:
            heapq.heappushpop(heap, c)
        else:
            heapq.heappush(heap, c)

print(heapq.heappop(heap))
