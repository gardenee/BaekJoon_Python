from sys import stdin

N, K = map(int, input().split())
result = []
info = []

for _ in range(N):
    ipt = list(map(int, stdin.readline().split()))
    result.append(ipt[1:])
    if ipt[0] == K: info = ipt[1:]

result.sort(reverse=True)
print(result.index(info)+1)
