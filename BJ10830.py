def multilpy(a, b, N):
    rtn = [[0] * N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            for n in range(N):
                rtn[i][j] += a[i][n] * b[n][j]
                rtn[i][j] %= 1000

    return rtn


N, B = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]
answer = [[0] * N for _ in range(N)]
for i in range(N):
    answer[i][i] = 1

i, x = 0, B
mod = []
while x > 0:
    if x % 2 == 1:
        mod.append(i)
    x //= 2
    i += 1

for i in range(mod[-1]+1):
    if i in mod:
        answer = multilpy(answer, A, N)
    A = multilpy(A, A, N)

for i in range(N):
    for j in range(N):
        print(answer[i][j], end=" ")
    print()
