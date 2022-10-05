from sys import stdin
import heapq

N = int(input())
heap = []
pm = dict()

for _ in range(N):
    num = int(stdin.readline())
    if num == 0:
        if not heap:
            print(0)
        else:
            check = heapq.heappop(heap)
            if pm[check][0] > 0:
                print(-check)
                pm[check][0] -= 1
            else:
                print(check)
                pm[check][1] -= 1
    else:
        pm.setdefault(abs(num), [0] * 2)
        heapq.heappush(heap, abs(num))
        if num > 0:
            pm[num][1] += 1
        else:
            pm[-num][0] += 1
