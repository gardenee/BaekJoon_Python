from sys import stdin

N, M = map(int, input().split())
arr = list(map(int, input().split()))
for i in range(1, N):
    arr[i] += arr[i-1]

for _ in range(M):
    s, e = map(int, stdin.readline().split())
    if s == 1:
        print(arr[e-1])
    else:
        print(arr[e-1]-arr[s-2])
