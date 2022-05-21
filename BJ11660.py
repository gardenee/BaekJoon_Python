from sys import stdin

N, M = map(int, input().split())

arr = [[0] for _ in range(N+1)]
arr[0] += [0] * N
for i in range(1, N+1):
    arr[i] += list(map(int, stdin.readline().split()))
    for j in range(1, N+1):
        arr[i][j] += arr[i][j-1]
    for j in range(1, N+1):
        arr[i][j] += arr[i-1][j]

ans = ""
for _ in range(M):
    a, b, c, d = map(int, stdin.readline().split())
    ans += str(arr[c][d] - arr[a-1][d] - arr[c][b-1] + arr[a-1][b-1]) + "\n"

print(ans)
