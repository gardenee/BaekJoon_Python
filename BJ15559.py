def find_parents(X):
    global parents
    if parents[X] == X:
        return X
    parents[X] = find_parents(parents[X])
    return parents[X]


def union(X, Y):
    global parents
    parents[find_parents(X)] = find_parents(Y)


N, M = map(int, input().split())
board = [list(input()) for _ in range(N)]

ref = {"N": 0, "W": 1, "E": 2, "S": 3}
dx, dy = [-1, 0, 0, 1], [0, -1, 1, 0]

parents = [i for i in range(N*M)]

for x in range(N):
    for y in range(M):
        n = ref[board[x][y]]
        nx, ny = x+dx[n], y+dy[n]
        if 0 <= nx < N and 0 <= ny < M:
            union(M*x+y, M*nx+ny)

answer = set()
for i in range(N*M):
    answer.add(find_parents(i))

print(len(answer))
