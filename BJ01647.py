from sys import stdin
import heapq


def find_parents(X):
    global parents
    if parents[X] == X:
        return X
    parents[X] = find_parents(parents[X])
    return parents[X]


def union(X, Y):
    global parents
    parents[find_parents(X)] = find_parents(Y)


N, M = map(int, input().split())
parents = [i for i in range(N+1)]
heap = []

for _ in range(M):
    A, B, C = map(int, stdin.readline().split())
    heapq.heappush(heap, [C, A, B])

cnt, answer = 0, 0
while cnt < N-2:
    C, A, B = heapq.heappop(heap)
    if find_parents(A) == find_parents(B):
        continue
    union(A, B)
    answer += C
    cnt += 1

print(answer)
