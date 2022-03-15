import sys

N, C = map(int, input().split())
arr = (C+1) * [0]
for _ in range(N):
    t = int(sys.stdin.readline())
    for i in range(t, C+1, t):
        arr[i] = 1

print(arr.count(1))
