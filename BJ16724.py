import sys
sys.setrecursionlimit(10 ** 5)

N, M = map(int, input().split())
board = [list(input()) for _ in range(N)]
parents = [i for i in range(N*M)]

ref = {"U": 0, "D": 1, "L": 2, "R": 3}
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]


def find_parents(X):
    global parents
    if parents[X] == X:
        return X
    parents[X] = find_parents(parents[X])
    return parents[X]


def union(X, Y):
    global parents
    parents[find_parents(X)] = find_parents(Y)


def change_form(x, y):
    return M*x+y


for x in range(N):
    for y in range(M):
        n = ref[board[x][y]]
        nx, ny = x+dx[n], y+dy[n]
        if 0 <= nx < N and 0 <= ny < M:
            union(change_form(nx, ny), change_form(x, y))

roop = set()
for i in range(M*N):
    roop.add(find_parents(i))

print(len(roop))
