from sys import stdin

def find_parents(x):
    global parents
    if parents[x] == x:
        return x
    parents[x] = find_parents(parents[x])
    return parents[x]


def union(x, y):
    global parents
    parents[find_parents(x)] = find_parents(y)


N, M = int(input()), int(input())
graph = [[] for _ in range(N+1)]
parents = [i for i in range(N+1)]

for _ in range(M):
    a, b = map(int, stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)
    union(a, b)


groups = dict()
for i in range(1, N+1):
    idx = find_parents(i)
    groups.setdefault(idx, [])
    groups[idx].append(i)

print(len(groups))

answer = []
for key in groups.keys():
    group = groups[key]
    cnt = len(group)
    leader = -1

    for i in range(len(group)):
        curr = group[i]
        temp = 0
        check = {curr}
        prev = [curr]
        while len(check) < len(group):
            temp += 1
            next = []
            for p in prev:
                t = graph[p]
                for tt in t:
                    if tt not in check and tt in group:
                        check.add(tt)
                        next.append(tt)
            prev = next[:]

        if temp < cnt:
            cnt = temp
            leader = curr

    answer.append(leader)

answer.sort()
for a in answer:
    print(a)
