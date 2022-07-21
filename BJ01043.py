N, M = map(int, input().split())
truth = list(map(int, input().split()))
T = truth[0]
truth[0] = 0
group = dict()

parents = [0] * (N+1)
for i in range(N+1):
    parents[i] = i
    group[i] = list()

for t in truth:
    parents[t] = 0


def findparents(a):
    global parents
    if parents[a] == 0:
        return 0
    if parents[a] == a:
        return a
    parents[a] = findparents(parents[a])


def union(a, b):
    global parents
    if parents[a] == 0:
        parents[findparents(b)] = 0
    elif parents[b] == 0:
        parents[findparents(a)] = 0
    else:
        parents[findparents(a)] = findparents(b)


for j in range(M):
    curr = list(map(int, input().split()))
    n = curr[0]
    for i in range(1, n+1):
        group[curr[i]].append(j)
        if i == n:
            break
        union(curr[i+1], curr[i])

result = [1] * M
for i in range(1, N+1):
    curr = findparents(parents[i])
    if curr == 0:
        for g in group[i]:
            result[g] = 0

print(sum(result))
