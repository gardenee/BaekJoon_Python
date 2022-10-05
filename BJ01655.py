from sys import stdin
import heapq

N = int(input())
left, right = [], []
mid, a, b = 0, 0, 0

for i in range(N):
    num = int(stdin.readline())
    if i == 0:
        mid = num
    elif a >= b:
        heapq.heappush(left, -num)
        heapq.heappush(left, -mid)
        heapq.heappush(right, -heapq.heappop(left))
        mid = -heapq.heappop(left)
        b += 1
    else:
        heapq.heappush(right, mid)
        heapq.heappush(right, num)
        heapq.heappush(left, -heapq.heappop(right))
        mid = heapq.heappop(right)
        a += 1
    print(mid)
