from sys import stdin


def gdc(a, b):
    if b == 0:
        return a
    tmp = a
    a = b
    b = tmp % b
    return gdc(a, b)


N = int(input())
start, end = -1, -1
prev, gap = -1, -1

for i in range(N):
    curr = int(stdin.readline())

    if i == 0:
        start = curr
        prev = curr
        continue
    if i == 1:
        gap = curr - prev
        prev = curr
        continue
    if i == N-1:
        end = curr

    tmp = curr - prev
    gap = gdc(max(gap, tmp), min(gap, tmp))
    prev = curr

print((end-start)//gap - N + 1)
