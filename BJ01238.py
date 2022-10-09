import sys
sys.setrecursionlimit(10**5)
si = sys.stdin.readline

N, M, X = map(int, input().split())
tree = dict()
reverse = dict()
go = [10**5] * (N+1)
back = [10**5] * (N+1)

for _ in range(M):
    s, e, t = map(int, si().split())
    tree.setdefault(s, [])
    reverse.setdefault(e, [])
    tree[s].append([e, t])
    reverse[e].append([s, t])

go[X], back[X] = 0, 0


def check(node, result, ref, visited):
    visited[node] = True
    link = ref[node]
    for l in link:
        result[l[0]] = min(result[l[0]], result[node]+l[1])

    idx = smallest(result, visited)

    if idx == -1:
        return result
    else:
        return check(idx, result, ref, visited)


def smallest(lst, visited):
    idx, time = -1, 10**5
    for i in range(1, N+1):
        if not visited[i] and lst[i] < time:
            time = lst[i]
            idx = i

    return idx


go = check(X, go, tree, [False]*(N+1))
back = check(X, back, reverse, [False]*(N+1))

answer = 0
for i in range(1, N+1):
    answer = max(answer, go[i]+back[i])

print(answer)
