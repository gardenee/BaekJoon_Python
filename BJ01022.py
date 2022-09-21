r1, c1, r2, c2 = map(int, input().split())
N, M = max(abs(r1), abs(r2)), max(abs(c1), abs(c2))
X = max(N, M)

arr = [[0] * (2*X+1) for _ in range(2*X+1)]
arr[X][X] = 1

n, y, x = 1, X, X
for i in range(1, X+1):
    for j in range(2*i-1):
        n += 1
        x += 1
        arr[y][x] = n

    for j in range(2*i-1):
        n += 1
        y -= 1
        arr[y][x] = n

    for j in range(2*i):
        n += 1
        x -= 1
        arr[y][x] = n

    for j in range(2*i):
        n += 1
        y += 1
        arr[y][x] = n

for i in range(2*X):
    n += 1
    x += 1
    arr[y][x] = n

lst = [arr[c1+X][r1+X], arr[c1+X][r2+X], arr[c2+X][r1+X], arr[c2+X][r2+X]]
l = len(str(max(lst)))

for i in range(r1+X, r2+X+1):
    for j in range(c1+X, c2+X+1):
        print(str(arr[i][j]).rjust(l, ' '), end=" ")
    print("\n", end="")
