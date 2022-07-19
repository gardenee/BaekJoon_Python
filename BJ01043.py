N, M = map(int, input().split())
truth = list(map(int, input().split()))
T = truth[0]
truth[0] = -1
group = dict()

parents = [0] * (N+1)
for i in range(N+1):
    if i in truth:
        parents[i] = -1
    else:
        parents[i] = i
    group[i] = list()


def findparents(a):
    global parents
    if parents[a] == -1:
        return -1
    if parents[a] == a:
        return a
    parents[a] = parents[parents[a]]
    return findparents(parents[a])


def union(a, b):
    global parents
    if parents[a] == -1:
        parents[findparents(b)] = -1
    elif parents[b] == -1:
        parents[findparents(a)] = -1
    else:
        parents[findparents(a)] = findparents(b)


for j in range(M):
    curr = list(map(int, input().split()))
    n = curr[0]
    for i in range(1, n+1):
        group[curr[i]].append(chr(65+j))
        if i == n:
            break
        union(curr[i], curr[i+1])

answer = set()
for i in range(1, N+1):
    curr = findparents(parents[i])
    if curr != -1:
        for g in group[i]:
            answer.add(g)

print(len(answer))
