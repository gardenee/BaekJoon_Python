from sys import stdin


def find_parents(a):
    global parents

    if parents[a] == a:
        return a

    parents[a] = find_parents(parents[a])
    return parents[a]


def union(a, b):
    global parents

    a, b = find_parents(min(a, b)), find_parents(max(a, b))
    parents[b] = a


N, M, k = map(int, input().split())
A = list(map(int, input().split()))

parents = [i for i in range(N+1)]

for _ in range(M):
    v, w = map(int, stdin.readline().split())

    if find_parents(v) != find_parents(w):
        union(v, w)

friend_cost = dict()

for i in range(1, N+1):
    parent = find_parents(i)
    price = A[i-1]

    friend_cost.setdefault(parent, price)
    friend_cost[parent] = min(friend_cost[parent], price)

answer = 0

for key in friend_cost.keys():
    answer += friend_cost[key]

if answer > k:
    answer = "Oh no"

print(answer)
