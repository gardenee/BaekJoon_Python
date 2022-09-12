from collections import deque
from sys import stdin


def pDown(heap, i):
    leafR = 2*i + 2
    leafL = 2*i + 1

    if leafL < len(heap):
        if leafR < len(heap) and heap[leafR] < heap[leafL]:
            heap[leafL], heap[leafR] = heap[leafR], heap[leafL]
            heap = pDown(heap, leafR)
        if heap[i] > heap[leafL]:
            heap[i], heap[leafL] = heap[leafL], heap[i]
            heap = pDown(heap, leafL)

    return heap


N = int(input())
heap = deque([])

for _ in range(N):
    curr = list(map(int, stdin.readline().rstrip().split()))
    for c in curr:
        if heap.__len__() >= N:
            heap.appendleft(c)
            pDown(heap, 0)
            heap.popleft()
        else:
            heap.appendleft(c)
            pDown(heap, 0)

print(heap.popleft())
