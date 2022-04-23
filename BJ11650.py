from sys import stdin
N = int(input())
dic = {}
for _ in range(N):
    x, y = map(int, stdin.readline().split())
    dic.setdefault(x, [])
    dic[x].append(y)

X = list(dic.keys())
X.sort()
for i in range(len(X)):
    dic[X[i]].sort()

for i in range(len(X)):
    for j in range(len(dic[X[i]])):
        print(X[i], dic[X[i]][j])
