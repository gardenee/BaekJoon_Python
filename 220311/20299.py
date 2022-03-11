import sys

N, K, L = map(int, input().split())
num = 0
ans = ''

for _ in range(N):
    a, b, c = map(int, sys.stdin.readline().split())
    if min(a, b, c) >= L and (a + b + c) >= K:
        num += 1
        ans += str(a) + ' ' + str(b) + ' ' + str(c) + ' '

print(num)
print(ans)