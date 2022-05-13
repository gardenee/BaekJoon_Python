from sys import stdin

N, M = map(int, input().split())
ref = set()
for _ in range(N):
    ref.add(stdin.readline())

ans = 0
for _ in range(M):
    curr = stdin.readline()
    if curr in ref:
        ans += 1

print(ans)
