from sys import stdin
N = int(input())
dic = {}
for _ in range(N):
    n = int(stdin.readline())
    dic.setdefault(n, 0)
    dic[n] += 1

keys = list(dic.keys())
keys.sort()

for k in keys:
    for _ in range(dic[k]):
        print(k)
