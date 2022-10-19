from sys import stdin
import bisect

N, M = map(int, input().split())
name, hp = [], []
for _ in range(N):
    n, h = stdin.readline().split()
    if not hp or hp[-1] != int(h):
        hp.append(int(h))
        name.append(n)

for _ in range(M):
    h = int(stdin.readline())
    idx = bisect.bisect_left(hp, h)
    print(name[idx])
