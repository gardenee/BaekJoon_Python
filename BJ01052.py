import heapq

N, K = map(int, input().split())
answer = 0

if N == 1:
    answer = -1
else:
    n = N
    filled = [1] * N

    