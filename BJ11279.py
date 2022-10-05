from sys import stdin
import heapq

N = int(input())
heap = []

for _ in range(N):
    num = -1 * int(stdin.readline())
    if num == 0:
        if heap:
            print(-1 * heapq.heappop(heap))
        else:
            print(0)
    else:
        heapq.heappush(heap, num)
