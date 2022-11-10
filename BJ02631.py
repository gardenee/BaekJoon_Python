from sys import stdin
import bisect

N = int(input())
line = [int(stdin.readline()) for _ in range(N)]

lst = []
for l in line:
    if not lst or l > lst[-1]:
        lst.append(l)
    else:
        idx = bisect.bisect_left(lst, l)
        lst[idx] = l

print(N - len(lst))
