from sys import stdin

N = int(input())
tree = dict()

for _ in range(N-1):
    a, b = map(int, stdin.readline().split())
    tree.setdefault(a, list())
    tree.setdefault(b, list())
    tree[a].append(b)
    tree[b].append(a)

parents = [0] * (N+1)

cnt = 0
curr = [1]
while (True):
    temp = list()
    for parent in curr:
        if tree.get(parent):
            sons = tree[parent]
            for son in sons:
                if parents[son] == 0:
                    parents[son] = parent
                    temp.append(son)
                    cnt += 1
    if cnt == N:
        break
    curr = temp

for i in range(2, N+1):
    print(parents[i])
