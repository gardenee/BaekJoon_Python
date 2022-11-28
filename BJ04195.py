from sys import stdin


def find_parents(X):
    if X == parents[X]:
        return X
    else:
        return find_parents(parents[X])


def union(X, Y):
    global parents, cnt
    if find_parents(X) == find_parents(Y):
        return
    cnt[find_parents(Y)] += cnt[find_parents(X)]
    parents[find_parents(X)] = find_parents(Y)


for _ in range(int(input())):
    idx = dict()
    seq = 1
    parents = [0]
    cnt = dict()

    F = int(input())
    for _ in range(F):
        A, B = stdin.readline().split()

        if A not in idx:
            parents.append(seq)
            idx[A] = seq
            cnt[seq] = 1
            seq += 1
        if B not in idx:
            parents.append(seq)
            idx[B] = seq
            cnt[seq] = 1
            seq += 1

        a, b = find_parents(idx[A]), find_parents(idx[B])
        union(idx[A], idx[B])
        print(cnt[find_parents(idx[B])])
