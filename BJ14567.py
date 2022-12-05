from sys import stdin
from collections import deque

N, M = map(int, input().split())
next = [[] for _ in range(N+1)]
answer = [1] * (N+1)

for _ in range(M):
    A, B = map(int, stdin.readline().split())
    next[A].append(B)
    if answer[A]+1 > answer[B]:
        answer[B] = answer[A]+1
        queue = deque([B])
        while queue:
            curr = queue.popleft()
            for n in next[curr]:
                if answer[curr]+1 > answer[n]:
                    answer[n] = answer[curr]+1
                    queue.append(n)

print(*answer[1:])
