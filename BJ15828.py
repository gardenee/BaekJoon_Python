from sys import stdin
from collections import deque

N = int(input())
router = deque()

while True:
    ipt = int(stdin.readline())
    if ipt == -1: break

    if ipt == 0:
        router.popleft()
    elif len(router) == N:
        continue
    else:
        router.append(ipt)

if not router:
    print("empty")
for packet in router:
    print(packet, end=" ")
