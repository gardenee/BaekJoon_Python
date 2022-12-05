from sys import stdin


def find_parents(X):
    global parents
    if parents[X] == X:
        return X
    parents[X] = find_parents(parents[X])
    return parents[X]


def union(X, Y):
    global parents
    A, B = find_parents(X), find_parents(Y)
    if A == B:
        return 0
    cnt[A] += cnt[B]
    parents[B] = A
    return cnt[B] * (cnt[A]-cnt[B])


N, M, Q = map(int, input().split())
link = [[0, 0] for _ in range(M+1)]
parents = [i for i in range(N+1)]
cnt = [1 for _ in range(N+1)]
check = [True] * (M+1)
merge = []

for i in range(1, M+1):
    X, Y = map(int, stdin.readline().split())
    link[i] = [X, Y]

for _ in range(Q):
    n = int(stdin.readline())
    check[n] = False
    merge.append(link[n])

for i in range(1, M+1):
    if check[i]:
        X, Y = link[i]
        union(X, Y)

answer = 0
for _ in range(Q):
    X, Y = merge.pop()
    answer += union(X, Y)

print(answer)
