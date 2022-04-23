from sys import stdin
N = int(input())
dic = {}
for _ in range(N):
    x, y = map(int, stdin.readline().split())
    dic.setdefault(y, [])
    dic[y].append(x)

Y = list(dic.keys())
Y.sort()
for i in range(len(Y)):
    dic[Y[i]].sort()

for i in range(len(Y)):
    for j in range(len(dic[Y[i]])):
        print(dic[Y[i]][j], Y[i])
