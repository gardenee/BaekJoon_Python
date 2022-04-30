from sys import stdin
from collections import deque

L = int(input())
ML, MK = map(int, input().split())
gun = deque()
damage = 0
C = int(input())
flag = 1

for _ in range(L):
    curr = int(stdin.readline())
    if gun.__len__() >= ML:
        damage -= gun.popleft()

    if (curr - damage - MK) <= 0:
        gun.append(MK)
        damage += MK
    else:
        if C:
            gun.append(0)
            C -= 1
        else:
            flag = 0
            break

if flag == 1:
    print("YES")
else:
    print("NO")
