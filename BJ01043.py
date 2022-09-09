N, M = map(int, input().split())
parents = []
for i in range(N+1):
    parents.append(i)
groups = []

truth = list(map(int, input().split()))
for i in range(1, truth[0]+1):
    parents[truth[i]] = 0


def findparents(a):
    global parents
    if parents[a] == 0:
        return 0
    if parents[a] == a:
        return a
    return findparents(parents[a])


def union(a, b):
    global parents
    x = findparents(a)
    y = findparents(b)
    parents[max(x, y)] = min(x, y)


for _ in range(M):
    curr = list(map(int, input().split()))
    groups.append(curr[1:])
    for i in range(1, curr[0]):
        union(curr[i], curr[i+1])

cnt = 0
for i in range(M):
    for people in groups[i]:
        if findparents(people) == 0:
            cnt += 1
            break

print(M - cnt)
