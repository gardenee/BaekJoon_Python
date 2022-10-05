from sys import stdin
import heapq

N = int(input())
heap = []

for _ in range(N):
    num = int(stdin.readline())
    if num == 0:
        if heap: print(heapq.heappop(heap))
        else: print(0)
    else: heapq.heappush(heap, num)
