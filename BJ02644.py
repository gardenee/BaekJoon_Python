from sys import stdin
import heapq

n = int(input())
a, b = map(int, input().split())
down = dict()
up = dict()

for _ in range(int(input())):
    x, y = map(int, stdin.readline().split())
    down.setdefault(x, [])
    down[x].append(y)
    up.setdefault(y, [])
    up[y].append(x)

answer = -1
checked = set([a])
heap = [[0, a]]

while heap:
    cnt, curr = heapq.heappop(heap)
    if curr in down:
        for son in down[curr]:
            if son not in checked:
                checked.add(son)
                heapq.heappush(heap, [cnt+1, son])
            if son == b:
                answer = cnt+1

    if curr in up:
        for parent in up[curr]:
            if parent not in checked:
                checked.add(parent)
                heapq.heappush(heap, [cnt+1, parent])
            if parent == b:
                answer = cnt+1

    if answer != -1:
        break

print(answer)
